import React, { useState } from 'react';
import { uploadDocument, askQuestion } from './services/api';
import './App.css';

function App() {
  const [title, setTitle] = useState('');
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState('');
  const [uploadedFilePath, setUploadedFilePath] = useState('');
  const [answer, setAnswer] = useState('');

  const handleUpload = async () => {
    if (!title || !file) {
      alert('Please provide both a title and a file.');
      return;
    }
    try {
      const uploadedDocument = await uploadDocument(title, file);
      setUploadedFilePath(uploadedDocument.filepath);
    } catch (error) {
      console.error('Error uploading document:', error);
      alert('Failed to upload document.');
    }
  };

  const handleQuestion = async () => {
    if (!uploadedFilePath || !question) {
      alert('Please upload a document and provide a question.');
      return;
    }
    try {
      const response = await askQuestion(uploadedFilePath, question);
      setAnswer(response.answer);
    } catch (error) {
      console.error('Error asking question:', error);
      alert('Failed to get an answer.');
    }
  };

  return (
    <div className="App">
      <h2>Upload PDF Document</h2>
      <input
        type="text"
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <button onClick={handleUpload}>Upload</button>

      {uploadedFilePath && (
        <>
          <h2>Ask a Question</h2>
          <input
            type="text"
            placeholder="Question"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />
          <button onClick={handleQuestion}>Ask</button>
        </>
      )}

      {answer && <p>Answer: {answer}</p>}
    </div>
  );
}

export default App;
