import React, { useState } from 'react';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [isProcessing, setIsProcessing] = useState(false);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!file) {
      alert('Please select a file');
      return;
    }

    setIsProcessing(true);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('/upload', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        const error = await response.json();
        alert(`Error: ${error.error}`);
      } else {
        alert('File uploaded and processed successfully');
      }
    } catch (error) {
      alert