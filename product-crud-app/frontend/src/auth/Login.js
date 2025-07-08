import { useState } from "react";
import axios from "axios";
import toast from "react-hot-toast";

function Login() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);

    const handleLogin = async (e) => {
        e.preventDefault();
        setLoading(true);
        try {
            const response = await axios.post("http://127.0.0.1:8000/api/auth/login", {
                email,
                password
            }, {
                headers: { "Content-Type": "multipart/form-data", "Accept": "application/json" }
            });

            const token = response.data.access_token;
            localStorage.setItem("token", token);

            // Redirect to products page
            window.location.href = "/";
        } catch (err) {
            toast.error(err.response?.data?.detail || "Login failed.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-100 px-4">
            <div className="w-full max-w-md bg-white rounded-lg shadow-lg p-8">
                <h2 className="text-2xl font-bold text-center text-gray-800 mb-6">
                    Sign In to Your Account
                </h2>

                <form onSubmit={handleLogin}>
                    {/* Email */}
                    <div className="mb-4">
                        <label className="block text-sm text-gray-600 mb-1" htmlFor="email">
                            Email
                        </label>
                        <input
                            id="email"
                            type="email"
                            className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:border-blue-400"
                            placeholder="you@example.com"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                    </div>

                    {/* Password */}
                    <div className="mb-4">
                        <label className="block text-sm text-gray-600 mb-1" htmlFor="password">
                            Password
                        </label>
                        <input
                            id="password"
                            type="password"
                            className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:border-blue-400"
                            placeholder="********"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        />
                    </div>

                    {/* Submit Button */}
                    <div className="mb-4">
                        <button
                            type="submit"
                            className="w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700 transition duration-200"
                            disabled={loading}
                        >
                            {loading ? "Signing in..." : "Sign In"}
                        </button>
                    </div>

                    <div className="text-sm text-center">
                        <a href="/register" className="text-blue-500 hover:underline">
                            Don’t have an account? Register
                        </a>
                    </div>
                </form>
            </div>
        </div>
    );
}

export default Login;