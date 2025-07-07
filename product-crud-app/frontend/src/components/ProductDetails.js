const ProductDetails = ({ product }) => {
  if (!product) return null;

  return (
    <div className="rounded-lg bg-white">
      <div className="space-y-4">
        <div>
          {/* <h3 className="text-sm font-medium text-gray-600">Status</h3> */}
          <span
            className={`inline-flex items-center gap-1 rounded-full px-2 py-1 text-xs font-semibold ${product.is_available
              ? 'bg-green-100 text-green-800'
              : 'bg-red-100 text-red-800'
              }`}
          >
            <span
              className={`h-2 w-2 rounded-full ${product.is_available ? 'bg-green-500' : 'bg-red-500'
                }`}
            ></span>
            {product.is_available ? 'Available' : 'Unavailable'}
          </span>
        </div>
        
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
