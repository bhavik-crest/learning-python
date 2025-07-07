import React, { useEffect, useState } from "react";
import { createProduct, updateProduct } from "../api";
import toast from "react-hot-toast";

const empty = {
  name: "",
  description: "",
  price: "",
  is_available: true,
};

const ProductForm = ({ selectedProduct, onSuccess }) => {
  const [form, setForm] = useState(empty);
  const editing = Boolean(selectedProduct);

  useEffect(() => {
    setForm(editing ? selectedProduct : empty);
  }, [editing, selectedProduct]);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    const val = type === "checkbox" ? checked : value;
    setForm((prev) => ({ ...prev, [name]: val }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      editing
        ? await updateProduct(selectedProduct.id, form)
        : await createProduct(form);
      toast.success(`Product ${editing ? "updated" : "created"} successfully!`);
      onSuccess(); // refresh list + close modal
    } catch (err) {
      toast.error(`Could not save product`);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-5 p-2">
      <input
        name="name"
        value={form.name}
        onChange={handleChange}
        placeholder="Product name"
        autoComplete="off"
        required
        className="w-full rounded-md border px-3 py-2"
      />
      <textarea
        name="description"
        value={form.description}
        onChange={handleChange}
        placeholder="Product description"
        autoComplete="off"
        required
        className="w-full rounded-md border px-3 py-2"
      />
      <input
        name="price"
        type="number"
        value={form.price}
        onChange={handleChange}
        placeholder="Price"
        autoComplete="off"
        required
        className="w-full rounded-md border px-3 py-2"
      />

      <div className="flex items-center gap-3">
        <label className="relative inline-flex items-center cursor-pointer">
          <input
            type="checkbox"
            name="is_available"
            checked={form.is_available}
            onChange={handleChange}
            className="sr-only peer"
          />
          <div className="w-11 h-6 bg-gray-300 rounded-full peer peer-checked:bg-blue-600 transition-all" />
          <div className="absolute left-1 top-1 w-4 h-4 bg-white rounded-full transition-transform peer-checked:translate-x-full" />
        </label>
        <label htmlFor="is_available" className="text-sm font-medium text-gray-700">
          {form.is_available ? 'Available' : 'Unavailable'}
        </label>
      </div>

      <div className="flex justify-end gap-2">
        <button
          type="submit"
          className="rounded-md bg-blue-600 px-4 py-2 font-medium text-white hover:bg-blue-700"
        >
          {editing ? "Update" : "Add"}
        </button>
      </div>
    </form>
  );
};

export default ProductForm;
