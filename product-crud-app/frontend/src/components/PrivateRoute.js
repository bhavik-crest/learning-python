import { Navigate } from "react-router-dom";
import { isTokenValid } from "../utils/auth";

function PrivateRoute({ children }) {
  const isAuthenticated = isTokenValid();

  if (!isAuthenticated) {
    localStorage.removeItem("token");
    return <Navigate to="/login" replace />;
  }

  return children;
}

export default PrivateRoute;