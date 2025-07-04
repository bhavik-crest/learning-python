import React, { useEffect, useState } from "react";
import { fetchProducts, deleteProduct } from "../api";
import Swal from 'sweetalert2';
import toast from 'react-hot-toast';

const ProductList = ({ onEdit, onView, refreshKey }) => {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);

    const load = async () => {
        setLoading(true);
        try {
            const res = await fetchProducts();
            setProducts(res.data);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => { load(); }, [refreshKey]);

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

    if (!products.length) return <p>No products yet.</p>;

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


    return (
        <div className="overflow-x-auto">
            <table className="w-full table-auto border border-gray-200 shadow-sm rounded-md text-sm text-gray-800 bg-white">
                <thead className="bg-gray-100 text-gray-700 uppercase tracking-wider">
                    <tr>
                        {["#", "Name", "Description", "Price", "Actions"].map((h) => (
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
        </div>
    );

};

export default ProductList;
