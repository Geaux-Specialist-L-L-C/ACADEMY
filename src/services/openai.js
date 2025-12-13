import api from './api';

export const getAIResponse = async (prompt) => {
  try {
    const response = await api.post('/openai', { prompt }, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.REACT_APP_OPENAI_API_KEY}`
      }
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching AI response', error);
    throw error;
  }
};
