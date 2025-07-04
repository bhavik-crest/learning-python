const ProductDetails = ({ product }) => {
  if (!product) return null;

  return (
    <div className="rounded-lg bg-white p-2 space-y-4">
      <div className="space-y-3">
        <div>
          <h3 className="text-sm font-medium text-gray-600">Name</h3>
          <p className="text-base text-gray-800">{product.name}</p>
        </div>

        <div>
          <h3 className="text-sm font-medium text-gray-600">Description</h3>
          <p className="text-base text-gray-800">{product.description}</p>
        </div>

        <div>
          <h3 className="text-sm font-medium text-gray-600">Price</h3>
          <p className="text-base font-semibold">₹{product.price}</p>
        </div>
      </div>
    </div>
  );
};

export default ProductDetails;
