import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import { Toaster } from 'react-hot-toast';
import ProductList from "./components/ProductList";
import Login from "./auth/Login";
import Register from "./auth/Register";
import PrivateRoute from "./components/PrivateRoute";
import NotFound from "./NotFound";
import PublicRoute from "./components/PublicRoute";
import Navbar from "./components/Navbar";


function App() {
  const token = localStorage.getItem("token");

  return (
    <>
      <Router>
        <Navbar />

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

        <Routes>
          {/* Public Routes */}
          <Route
            path="/login"
            element={
              <PublicRoute>
                <Login />
              </PublicRoute>
            }
          />
          <Route
            path="/register"
            element={
              <PublicRoute>
                <Register />
              </PublicRoute>
            }
          />

          {/* Protected Route */}
          <Route
            path="/"
            element={
              <PrivateRoute>
                <ProductList />
              </PrivateRoute>
            }
          />

          {/* Catch-all 404 */}
          <Route path="*" element={<NotFound />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
