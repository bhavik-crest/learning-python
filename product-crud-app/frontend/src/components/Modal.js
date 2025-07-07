const Modal = ({ open, onClose, title, children }) => {
  if (!open) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm px-4">
      {/* Modal Container */}
      <div className="w-full max-w-2xl rounded-2xl bg-white shadow-2xl animate-fade-in scale-100">
        {/* Modal Header */}
        <div className="flex items-center justify-between bg-gradient-to-r from-blue-600 to-indigo-600 rounded-t-2xl px-4 py-3">
          <h2 className="text-lg sm:text-xl font-semibold text-white">{title}</h2>
          <button
            onClick={onClose}
            className="text-white text-xl font-bold hover:text-gray-200 transition"
            aria-label="Close modal"
          >
            ✕
          </button>
        </div>

        {/* Modal Content */}
        <div className="p-5 sm:p-6 overflow-y-auto max-h-[80vh] text-gray-800">
          {children}
        </div>
      </div>
    </div>
  );
};

export default Modal;