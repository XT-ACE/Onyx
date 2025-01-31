import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/form-records/';  // Ensure lowercase

export const signup = (user) => {
    return axios.post(API_URL, user);  // No extra "FormRecords/" in the URL
};


