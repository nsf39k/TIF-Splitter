import React from 'react';

const DownloadSquares = () => {
  const handleDownloadClick = () => {
    window.location.href = '/download';
  };

  return (
    <div>
      <button onClick={handleDownloadClick}>Download PNG Tiles</button>
    </div>
  );
};

export default DownloadSquares;