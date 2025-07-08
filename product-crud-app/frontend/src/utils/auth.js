import { jwtDecode } from "jwt-decode";

export function isTokenValid() {
  const token = localStorage.getItem("token");
  if (!token) return false;

  try {
    const decoded = jwtDecode(token);
    const isExpired = Date.now() >= decoded.exp * 1000;
    return !isExpired;
  } catch (err) {
    return false;
  }
}