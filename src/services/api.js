import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const uploadDocument = async (title, file) => {
  const formData = new FormData();
  formData.append('title', title);
  formData.append('file', file);

  try {
    const response = await axios.post(`${API_URL}/upload/`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  } catch (error) {
    console.error('Upload document error:', error);
    throw error;
  }
};

export const askQuestion = async (filepath, question) => {
  try {
    const response = await axios.post(`${API_URL}/ask/`, { filepath, question });
    return response.data;
  } catch (error) {
    console.error('Ask question error:', error);
    throw error;
  }
};
