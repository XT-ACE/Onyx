import axios from 'axios';

const API_URL = 'http://192.168.1.11:8000/api/form-records/';  // Ensure lowercase

export const signup = (user) => {
    return axios.post(API_URL, user);  // No extra "FormRecords/" in the URL
};


