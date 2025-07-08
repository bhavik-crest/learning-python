import { Navigate } from "react-router-dom";

function PublicRoute({ children }) {
  const token = localStorage.getItem("token");

  // If token exists, redirect to /products
  if (token) {
    return <Navigate to="/" replace />;
  }

  return children;
}

export default PublicRoute;