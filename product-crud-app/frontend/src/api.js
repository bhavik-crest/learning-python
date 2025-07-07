import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export const fetchProducts = (page = 1, limit = 10, search = "") => axios.get(`${API_URL}/products`, { params: { page, limit, search } });
export const createProduct = (product) => axios.post(`${API_URL}/products`, product);
export const updateProduct = (id, product) => axios.put(`${API_URL}/products/${id}`, product);
export const deleteProduct = (id) => axios.delete(`${API_URL}/products/${id}`);