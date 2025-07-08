import React, { use, useEffect, useRef, useState } from "react";
import { fetchProducts, deleteProduct } from "../api";
import Swal from 'sweetalert2';
import toast from 'react-hot-toast';
import Modal from "./Modal";
import ProductDetails from "./ProductDetails";
import ProductForm from "./ProductForm";

const ProductList = () => {

    //Modal
    const [modalOpen, setModalOpen] = useState(false);
    const [isView, setIsView] = useState(false);
    const [selectedProduct, setSelectedProduct] = useState(null);
    const [refreshKey, setRefreshKey] = useState(0);

    const openCreate = () => {
        setSelectedProduct(null);
        setModalOpen(true);
    };

    const openEdit = (product) => {
        setSelectedProduct(product);
        setModalOpen(true);
    };

    const openView = (product) => {
        setSelectedProduct(product);
        setModalOpen(true);
        setIsView(true);
    };

    const handleSuccess = () => {
        setModalOpen(false);
        setRefreshKey((k) => k + 1); // force list reload
    };

    const handleClose = () => {
        setModalOpen(false);
        setSelectedProduct(null);
        setIsView(false);
    };


    // Static array
    const perPageList = [5, 10, 15, 20, 25, 30, 50]; // Per page
    const tableHeader = ["#", "Name", "Description", "Price", "Status", "Actions"]; // Table header

    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [pageSize, setPageSize] = useState(10); // Default page size
    const [page, setPage] = useState(1);
    const [pages, setPages] = useState(1); // total pages
    const [search, setSearch] = useState("");
    const inputRef = useRef(null);


    // Display Data
    const load = async (p = page, size = pageSize, term = search) => {
        setLoading(true);
        try {
            const res = await fetchProducts(p, size, term);
            setProducts(res.data.items);
            setPages(res.data.pages);
            setPage(res.data.page);
        } finally {
            setLoading(false);
        }
    };

    // Update list on page, pageSize, refreshKey value change
    useEffect(() => { load(); }, [refreshKey]);

    // Manage set timeout when searching or pagination
    useEffect(() => {
        setLoading(true);
        const timeout = setTimeout(() => load(), 400);
        return () => clearTimeout(timeout);
    }, [search, page, pageSize]);

    // Manage search box auto focus
    useEffect(() => {
        if (!loading) inputRef.current?.focus();
    }, [loading]);

    // Delete product based on product id
    const remove = async (id) => {
        const result = await Swal.fire({
            title: 'Are you sure?',
            text: 'You won’t be able to undo this!',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#d33',
            cancelButtonColor: '#aaa',
            confirmButtonText: 'Yes, delete it!',
        });

        if (result.isConfirmed) {
            try {
                await deleteProduct(id);
                setProducts(products.filter((p) => p.id !== id));

                toast.success('Product has been deleted.');
            } catch (err) {
                if (err.response?.status === 404) {
                    const { code, message } = err.response.data.detail;
                    toast.error(message);
                } else {
                    toast.error('Delete failed.');
                }
            }
        }
    };

    // Manage page number with ellipsis(.....)
    const getPageList = (page, pages) => {
        const visible = new Set();

        // First 3 pages
        for (let i = 1; i <= Math.min(3, pages); i++) visible.add(i);

        // Current page ±1
        for (let i = page - 1; i <= page + 1; i++) {
            if (i > 0 && i <= pages) visible.add(i);
        }

        // Last 3 pages
        for (let i = Math.max(1, pages - 2); i <= pages; i++) visible.add(i);

        // Convert to sorted array
        const sorted = [...visible].sort((a, b) => a - b);

        // Insert ellipsis tokens
        const result = [];
        for (let i = 0; i < sorted.length; i++) {
            result.push(sorted[i]);
            if (i < sorted.length - 1 && sorted[i + 1] !== sorted[i] + 1) {
                result.push("ellipsis");
            }
        }

        return result;
    };

    // Render Page
    return (
        <div className="w-full p-5">
            <div className="flex items-center justify-between mb-6">
                <h1 className="text-2xl font-bold text-gray-800"></h1>

                <button
                    onClick={openCreate}
                    className="rounded-md bg-green-600 px-4 py-2 font-medium text-white hover:bg-green-700"
                >
                    + Add Product
                </button>
            </div>

            <div className="bg-gradient-to-br from-blue-50 via-indigo-50 to-blue-100 p-4 rounded-xl shadow-md">
                {/* Top Controls */}
                <div className="flex flex-col md:flex-row justify-between items-center mb-4 gap-4">
                    {/* Per Page Dropdown */}
                    <div className="w-full md:w-auto flex items-center gap-2">
                        <label className="text-sm font-medium text-gray-700 whitespace-nowrap">Show per page:</label>
                        <select
                            value={pageSize}
                            onChange={(e) => {
                                setPageSize(Number(e.target.value));
                                setPage(1);
                            }}
                            className="w-full md:w-auto border border-gray-300 rounded-md px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
                        >
                            {perPageList.map((size) => (
                                <option key={size} value={size}>
                                    {size}
                                </option>
                            ))}
                        </select>
                    </div>

                    {/* Search Bar */}
                    <div className="w-full md:w-80 relative">
                        {/* Search Input */}
                        <input
                            type="text"
                            ref={inputRef}
                            value={search}
                            placeholder="Search products..."
                            onChange={(e) => {
                                setSearch(e.target.value);
                                setPage(1);
                            }}
                            className="w-full border border-gray-300 rounded-md px-4 py-2 pr-10 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-400 shadow-sm"
                        />

                        {/* Clear Icon inside input */}
                        {search && (
                            <button
                                type="button"
                                onClick={() => {
                                    setSearch("");
                                    setPage(1);
                                    inputRef.current?.focus();
                                }}
                                className="absolute inset-y-0 right-2 flex items-center text-gray-400 hover:text-gray-600 focus:outline-none"
                            >
                                ✕
                            </button>
                        )}
                    </div>

                </div>

                {/* Product list table */}
                <div className="w-full overflow-x-auto rounded-md shadow-sm">
                    <table className="min-w-full text-sm text-gray-800 bg-white rounded-md">
                        <thead className="bg-gradient-to-r from-blue-600 to-indigo-600 text-white uppercase tracking-wider">
                            <tr>
                                {tableHeader.map((h) => (
                                    <th key={h} className="px-4 py-3 text-left font-semibold border border-indigo-200/40 whitespace-nowrap">
                                        {h}
                                    </th>
                                ))}
                            </tr>
                        </thead>
                        <tbody>
                            {!loading && !products.length && (
                                <tr>
                                    <td colSpan={6} className="px-4 py-5 text-center text-gray-600 font-medium">
                                        No product found.
                                    </td>
                                </tr>
                            )}

                            {loading && (
                                <tr>
                                    <td colSpan={6} className="px-4 py-5 text-center text-gray-600 font-medium">
                                        <div className="flex flex-col items-center justify-center h-20 space-y-2">
                                            <div className="flex space-x-2">
                                                <div className="h-3 w-3 rounded-full bg-blue-500 animate-bounce [animation-delay:-0.3s]"></div>
                                                <div className="h-3 w-3 rounded-full bg-blue-500 animate-bounce [animation-delay:-0.15s]"></div>
                                                <div className="h-3 w-3 rounded-full bg-blue-500 animate-bounce"></div>
                                            </div>
                                            <p className="text-sm text-gray-600">Loading products...</p>
                                        </div>
                                    </td>
                                </tr>
                            )}


                            {!loading && products.length > 0 && products.map((p) => (
                                <tr key={p.id} className="hover:bg-indigo-50 transition-colors border-t border-gray-100">
                                    <td className="border border-gray-200 px-4 py-3 whitespace-nowrap">#PID7894561230{p.id}</td>
                                    <td className="border border-gray-200 px-4 py-3">{p.name}</td>
                                    <td className="border border-gray-200 px-4 py-3 max-w-xs truncate text-gray-700" title={p.description}>
                                        {p.description}
                                    </td>
                                    <td className="border border-gray-200 px-4 py-3 font-medium whitespace-nowrap">₹{p.price}</td>
                                    <td className="border border-gray-200 px-4 py-3 font-medium whitespace-nowrap">
                                        <span
                                            className={`inline-flex items-center gap-1 rounded-full px-2 py-1 text-xs font-semibold ${p.is_available
                                                ? "bg-green-100 text-green-800"
                                                : "bg-red-100 text-red-800"
                                                }`}
                                        >
                                            <span className={`h-2 w-2 rounded-full ${p.is_available ? "bg-green-500" : "bg-red-500"}`}></span>
                                            {p.is_available ? "Available" : "Unavailable"}
                                        </span>
                                    </td>
                                    <td className="px-4 py-3 flex gap-2 items-center justify-start flex-wrap">
                                        <button
                                            onClick={() => openView(p)}
                                            className="flex h-8 w-8 items-center justify-center rounded-full bg-gradient-to-br from-gray-600 to-gray-800 text-white hover:brightness-110"
                                            title="View"
                                        >
                                            <i className="fa fa-info text-xs"></i>
                                        </button>
                                        <button
                                            onClick={() => openEdit(p)}
                                            className="flex h-8 w-8 items-center justify-center rounded-full bg-gradient-to-br from-blue-500 to-blue-700 text-white hover:brightness-110"
                                            title="Edit"
                                        >
                                            <i className="fa fa-edit text-xs"></i>
                                        </button>
                                        <button
                                            onClick={() => remove(p.id)}
                                            className="flex h-8 w-8 items-center justify-center rounded-full bg-gradient-to-br from-red-500 to-red-700 text-white hover:brightness-110"
                                            title="Delete"
                                        >
                                            <i className="fa fa-trash text-xs"></i>
                                        </button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>

                {/* Bottom Controls */}
                <div className="flex flex-col md:flex-row justify-between items-center mt-4 gap-4">
                    {/* Per Page Dropdown (bottom) */}
                    <div className="w-full md:w-auto flex items-center gap-2">
                        <label className="text-sm font-medium text-gray-700 whitespace-nowrap">Show per page:</label>
                        <select
                            value={pageSize}
                            onChange={(e) => {
                                setPageSize(Number(e.target.value));
                                setPage(1);
                            }}
                            className="w-full md:w-auto border border-gray-300 rounded-md px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
                        >
                            {perPageList.map((size) => (
                                <option key={size} value={size}>
                                    {size}
                                </option>
                            ))}
                        </select>
                    </div>

                    {/* Pagination */}
                    {products.length > 0 && (
                        <nav className="flex flex-wrap items-center justify-center gap-2 select-none" >
                            <button
                                disabled={page === 1}
                                onClick={() => setPage(page - 1)}
                                className={`px-3 py-1 rounded-md text-sm font-medium border ${page === 1
                                    ? "cursor-not-allowed bg-gray-200 text-gray-500"
                                    : "bg-gradient-to-r from-blue-500 to-blue-600 text-white hover:brightness-110"
                                    }`}
                            >
                                Prev
                            </button>

                            {getPageList(page, pages).map((item, idx) =>
                                item === "ellipsis" ? (
                                    <span key={`ellipsis-${idx}`} className="px-2 text-gray-500 select-none">
                                        …
                                    </span>
                                ) : (
                                    <button
                                        key={item}
                                        onClick={() => setPage(item)}
                                        className={`px-3 py-1 rounded-md text-sm font-medium border ${item === page
                                            ? "bg-indigo-600 text-white"
                                            : "bg-white hover:bg-gray-100"
                                            }`}
                                    >
                                        {item}
                                    </button>
                                )
                            )}

                            <button
                                disabled={page === pages}
                                onClick={() => setPage(page + 1)}
                                className={`px-3 py-1 rounded-md text-sm font-medium border ${page === pages
                                    ? "cursor-not-allowed bg-gray-200 text-gray-500"
                                    : "bg-gradient-to-r from-blue-500 to-blue-600 text-white hover:brightness-110"
                                    }`}
                            >
                                Next
                            </button>
                        </nav>
                    )}
                </div>
            </div>

            <Modal
                open={modalOpen}
                onClose={handleClose}
                title={isView ? '📦 Product Details' : (selectedProduct ? "Edit Product" : "Add Product")}
            >
                {
                    isView ? <ProductDetails
                        product={selectedProduct}
                    /> : <ProductForm
                        selectedProduct={selectedProduct}
                        onSuccess={handleSuccess}
                    />
                }

            </Modal>
        </div>
    );
};

export default ProductList;
