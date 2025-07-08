import { useLocation, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import { jwtDecode } from "jwt-decode";

function Navbar() {
    const location = useLocation();
    const navigate = useNavigate();
    const token = localStorage.getItem("token");

    const [email, setEmail] = useState("");
    const [dropdownOpen, setDropdownOpen] = useState(false);

    useEffect(() => {
        if (token) {
            try {
                const decoded = jwtDecode(token);
                setEmail(decoded.email || "");
            } catch {
                setEmail("");
            }
        }
    }, [token]);

    const handleLogout = () => {
        localStorage.removeItem("token");
        navigate("/login");
    };

    // Hide navbar on login & register routes
    if (location.pathname === "/login" || location.pathname === "/register") {
        return null;
    }

    return (
        <nav className="bg-white shadow-md px-6 py-3 flex items-center justify-between">
            <div
                className="text-xl font-bold cursor-pointer"
                onClick={() => navigate("/")}
            >
                🛍️ Product Management
            </div>

            {email && (
                <div className="relative">
                    <button
                        onClick={() => setDropdownOpen(!dropdownOpen)}
                        className="flex items-center gap-2 bg-gray-100 px-4 py-2 rounded-md hover:bg-gray-200 transition"
                    >
                        <span className="text-sm text-gray-800">{email}</span>
                        <svg
                            className={`w-4 h-4 transform transition-transform ${dropdownOpen ? "rotate-180" : ""
                                }`}
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                        >
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 9l-7 7-7-7" />
                        </svg>
                    </button>

                    {dropdownOpen && (
                        <div className="absolute right-0 mt-2 w-40 bg-white shadow-lg rounded-md z-50">
                            <button
                                onClick={handleLogout}
                                className="w-full text-left px-4 py-2 hover:bg-gray-100 text-sm"
                            >
                                Logout
                            </button>
                        </div>
                    )}
                </div>
            )}
        </nav>
    );
}

export default Navbar;
