import React, { useState } from "react";
import { Toaster } from 'react-hot-toast';
import ProductList from "./components/ProductList";
import ProductForm from "./components/ProductForm";
import Modal from "./components/Modal";
import ProductDetails from "./components/ProductDetails";

function App() {
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

  return (
    <>
      <Toaster
        position="top-center"
        toastOptions={{
          className: 'text-md',
          style: {
            background: '#1f2937', // Tailwind `bg-gray-800`
            border: '1px solid #4b5563', // Tailwind `border-gray-600`
            color: '#f3f4f6', // Tailwind `text-gray-200`
          },
        }}
      />

      <div className="w-full p-5">
        <div className="flex items-center justify-between mb-6">
          <h1 className="text-2xl font-bold text-gray-800">🛍️ Product Management</h1>

          <button
            onClick={openCreate}
            className="rounded-md bg-green-600 px-4 py-2 font-medium text-white hover:bg-green-700"
          >
            + Add Product
          </button>
        </div>


        <ProductList
          onEdit={openEdit}
          onView={openView}
          refreshKey={refreshKey}
        />

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
    </>
  );
}

export default App;
