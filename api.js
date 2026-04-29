import axios from "axios";

const API = "http://localhost:8000";

export const askQuestion = (data) =>
  axios.post(`${API}/chat`, data);

export const uploadFile = (file) => {
  const formData = new FormData();
  formData.append("file", file);
  return axios.post(`${API}/upload`, formData);
};