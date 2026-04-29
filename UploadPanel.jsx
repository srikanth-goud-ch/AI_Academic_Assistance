import { uploadFile } from "../api";

export default function UploadPanel() {
  const handleUpload = async (e) => {
    const file = e.target.files[0];
    await uploadFile(file);
    alert("Uploaded!");
  };

  return (
    <div>
      <h3>Upload PDF</h3>
      <input type="file" onChange={handleUpload} />
    </div>
  );
}