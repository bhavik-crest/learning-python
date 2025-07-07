import React, { use, useEffect, useState } from "react";
import { fetchProducts, deleteProduct } from "../api";
import Swal from 'sweetalert2';
import toast from 'react-hot-toast';

const ProductList = ({ onEdit, onView, refreshKey }) => {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [pageSize, setPageSize] = useState(5); // Default page size
    const [page, setPage] = useState(1);
    const [pages, setPages] = useState(1); // total pages
    const [perPageList, setPerPageList] = useState([5, 10, 15, 20, 25, 30, 50]);

    // Display Data
    const load = async (p = page, size = pageSize) => {
        setLoading(true);
        try {
            const res = await fetchProducts(p, size);
            setProducts(res.data.items);
            setPages(res.data.pages);
            setPage(res.data.page);
        } finally {
            setLoading(false);
        }
    };

    // Update list on page, pageSize, refreshKey value change
    useEffect(() => { load(); }, [page, pageSize, refreshKey]);

    // Show loader
    if (loading)
        return (
            <div className="flex flex-col items-center justify-center h-40 space-y-2">
                <div className="flex space-x-2">
                    <div className="h-3 w-3 rounded-full bg-blue-500 animate-bounce [animation-delay:-0.3s]"></div>
                    <div className="h-3 w-3 rounded-full bg-blue-500 animate-bounce [animation-delay:-0.15s]"></div>
                    <div className="h-3 w-3 rounded-full bg-blue-500 animate-bounce"></div>
                </div>
                <p className="text-sm text-gray-600">Loading products...</p>
            </div>
        );

    // Show no data message when data list is empty or null
    if (!products.length) return <p>No products yet.</p>;

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

    // Render Page
    return (
        <div className="overflow-x-auto">
            <div className="flex justify-between items-center my-4">
                {/* Per Page Dropdown */}
                <div>
                    <label className="text-sm mr-2 font-medium">Show per page:</label>
                    <select
                    value={pageSize}
                    onChange={(e) => {
                        setPageSize(Number(e.target.value));
                        setPage(1); // Reset to first page when page size changes
                    }}
                    className="border border-gray-300 rounded px-2 py-1 text-sm"
                    >
                    {perPageList.map((size) => (
                        <option key={size} value={size}>
                        {size}
                        </option>
                    ))}
                    </select>
                </div>

                {/* Search Bar */}
                <div className="w-full md:w-80">
                    <input
                    type="text"
                    placeholder="Search products..."
                    className="w-full border border-gray-300 rounded px-3 py-2 text-sm"
                    />
                </div>
            </div>

            {/* Product list table */}
            <table className="w-full table-auto border border-gray-200 shadow-sm rounded-md text-sm text-gray-800 bg-white">
                <thead className="bg-gray-100 text-gray-700 uppercase tracking-wider">
                    <tr>
                        {["#", "Name", "Description", "Price", 'Status', "Actions"].map((h) => (
                            <th key={h} className="px-4 py-3 text-left font-semibold border border-gray-200">
                                {h}
                            </th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {products.map((p) => (
                        <tr
                            key={p.id}
                            className="hover:bg-gray-50 transition-colors border-t border-gray-100"
                        >
                            <td className="border border-gray-200 px-4 py-3">#PID7894561230{p.id}</td>
                            <td className="border border-gray-200 px-4 py-3">{p.name}</td>
                            <td
                                className="border border-gray-200 px-4 py-3 max-w-xs truncate text-gray-700"
                                title={p.description}
                            >
                                {p.description}
                            </td>
                            <td className="border border-gray-200 px-4 py-3 font-medium">
                                ₹{p.price}
                            </td>
                            <td className="border border-gray-200 px-4 py-3 font-medium">
                                <span
                                    className={`inline-flex items-center gap-1 rounded-full px-2 py-1 text-xs font-semibold ${p.is_available
                                        ? 'bg-green-100 text-green-800'
                                        : 'bg-red-100 text-red-800'
                                        }`}
                                >
                                    <span
                                        className={`h-2 w-2 rounded-full ${p.is_available ? 'bg-green-500' : 'bg-red-500'
                                            }`}
                                    ></span>
                                    {p.is_available ? 'Available' : 'Unavailable'}
                                </span>
                            </td>
                            <td className="px-4 py-3 flex gap-3 items-center">
                                <button
                                    onClick={() => onView(p)}
                                    className="flex h-8 w-8 items-center justify-center rounded-full bg-gray-600 text-white hover:bg-gray-700"
                                    title="View"
                                >
                                    <i className="fa fa-info text-xs"></i>
                                </button>
                                <button
                                    onClick={() => onEdit(p)}
                                    className="flex h-8 w-8 items-center justify-center rounded-full bg-blue-600 text-white hover:bg-blue-700"
                                    title="Edit"
                                >
                                    <i className="fa fa-edit text-xs"></i>
                                </button>
                                <button
                                    onClick={() => remove(p.id)}
                                    className="flex h-8 w-8 items-center justify-center rounded-full bg-red-600 text-white hover:bg-red-700"
                                    title="Delete"
                                >
                                    <i className="fa fa-trash text-xs"></i>
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>

            <div className="flex justify-between items-center mt-4">
                {/* Per Page Dropdown */}
                <div>
                    <label className="text-sm mr-2 font-medium">Show per page:</label>
                    <select
                    value={pageSize}
                    onChange={(e) => {
                        setPageSize(Number(e.target.value));
                        setPage(1); // Reset to first page when page size changes
                    }}
                    className="border border-gray-300 rounded px-2 py-1 text-sm"
                    >
                    {perPageList.map((size) => (
                        <option key={size} value={size}>
                        {size}
                        </option>
                    ))}
                    </select>
                </div>

                {/* Pagination Bar */}
                <nav className="mt-4 flex items-center justify-center gap-2 select-none">
                    <button
                        disabled={page === 1}
                        onClick={() => setPage(page - 1)}
                        className={`px-3 py-1 rounded-md border ${page === 1
                            ? "cursor-not-allowed bg-gray-200 text-gray-500"
                            : "bg-white hover:bg-gray-100"
                            }`}
                    >
                        Prev
                    </button>

                    {[...Array(pages)].map((_, i) => {
                        const n = i + 1;
                        return (
                            <button
                                key={n}
                                onClick={() => setPage(n)}
                                className={`px-3 py-1 rounded-md border ${n === page
                                    ? "bg-blue-600 text-white"
                                    : "bg-white hover:bg-gray-100"
                                    }`}
                            >
                                {n}
                            </button>
                        );
                    })}

                    <button
                        disabled={page === pages}
                        onClick={() => setPage(page + 1)}
                        className={`px-3 py-1 rounded-md border ${page === pages
                            ? "cursor-not-allowed bg-gray-200 text-gray-500"
                            : "bg-white hover:bg-gray-100"
                            }`}
                    >
                        Next
                    </button>
                </nav>
            </div>
        </div>
    );

};

export default ProductList;
