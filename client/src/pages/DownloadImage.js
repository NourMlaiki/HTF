import React from "react";

function DownloadImage() {
  const handleDownload = () => {
    window.location.href = "http://127.0.0.1:5000/download/image";
  };

  return (
    <div>
      <h2>Download Sample Image</h2>
      <button onClick={handleDownload}>Download Image</button>
    </div>
  );
}

export default DownloadImage;
