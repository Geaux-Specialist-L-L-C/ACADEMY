// File: /geaux-academy/geaux-academy/src/utils/api.ts
// Description: Exports functions for making API calls, handling requests and responses, and managing error handling.
// Author: [Your Name]
// Created: [Date]

import axios from 'axios';

const API_BASE_URL = 'https://api.example.com'; // Replace with your API base URL

export const fetchData = async (endpoint: string) => {
    try {
        const response = await axios.get(`${API_BASE_URL}${endpoint}`);
        return response.data;
    } catch (error) {
        handleError(error);
    }
};

export const postData = async (endpoint: string, data: any) => {
    try {
        const response = await axios.post(`${API_BASE_URL}${endpoint}`, data);
        return response.data;
    } catch (error) {
        handleError(error);
    }
};

const handleError = (error: any) => {
    // Handle error appropriately (e.g., log it, show a notification)
    console.error('API call error:', error);
    throw error; // Rethrow the error for further handling if needed
};