import React from "react";

const Modal = ({ open, onClose, title, children }) => {
  if (!open) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40 backdrop-blur-sm">
      {/* modal box */}
      <div className="w-full max-w-lg rounded-2xl bg-white shadow-xl">
        <div className="mb-1 flex items-center justify-between bg-blue-700 rounded-t-2xl p-2 text-white">
          <h2 className="text-xl font-semibold">{title}</h2>
          <button
            onClick={onClose}
            className="rounded-full p-1 text-white p-2"
          >
            ✕
          </button>
        </div>
        <div className="p-2">
          {children}
        </div>
      </div>
    </div>
  );
};

export default Modal;
