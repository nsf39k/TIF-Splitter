import React, { useState } from 'react';

const UploadGeotiff = ({ onUploadSuccess }) => {
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
        onUploadSuccess();
        alert('File uploaded and processed successfully');
      }
    } catch (error) {
      alert(`Error: ${error.message}`);
    } finally {
      setIsProcessing(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="file">Select a GeoTIFF file:</label>
      <input type="file" id="file" name="file" accept=".tiff,.tif" onChange={handleFileChange} />
      <button type="submit" disabled={isProcessing}>
        {isProcessing ? 'Processing...' : 'Upload and Process'}
      </button>
    </form>
  );
};

export default UploadGeotiff;