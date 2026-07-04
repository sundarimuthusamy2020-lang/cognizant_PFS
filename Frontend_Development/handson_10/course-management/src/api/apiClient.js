import axios from "axios";

const apiClient = axios.create({
  baseURL: "https://jsonplaceholder.typicode.com",
  timeout: 5000,
  headers: {
    "Content-Type": "application/json",
  },
});

// Request Interceptor
apiClient.interceptors.request.use(
  (config) => {
    config.headers.Authorization = "Bearer mock-token-123";
    return config;
  },
  (error) => Promise.reject(error)
);

// Response Interceptor
apiClient.interceptors.response.use(
  (response) => response.data,
  (error) => {
    const err = new Error(
      error.response?.data?.message || "Something went wrong"
    );

    err.statusCode = error.response?.status || 500;

    return Promise.reject(err);
  }
);

export default apiClient;