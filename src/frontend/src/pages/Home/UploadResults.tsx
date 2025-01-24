import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Button, Upload, Typography, Form } from "antd";
import { UploadOutlined } from "@ant-design/icons";
import "./UploadResults.css"; // Custom CSS for styling

const { Title, Paragraph } = Typography;

const UploadResults: React.FC = () => {
  const navigate = useNavigate();
  const [resultsFile, setResultsFile] = useState<File | null>(null);

  const handleResultsFileUpload = (file: File) => {
    setResultsFile(file);
    console.log("Results file uploaded:", file);
    return false; // Prevent automatic upload
  };

  const handleResultsClick = () => {
    if (!resultsFile) {
      window.alert("Please upload a results file first.");
      return;
    }
    console.log("Viewing results...");
    navigate("/results");
  };

  return (
    <div className="upload-results-container">
      <div className="upload-results-card">
        <Title level={2} className="upload-results-title">
          View Results
        </Title>
        <Paragraph className="upload-results-description">
          Check the analysis results of your previous submissions by uploading
          the results ZIP file emailed to you.
        </Paragraph>

        <div className="upload-results-upload">
          <Upload.Dragger
            name="file"
            accept=".zip"
            beforeUpload={handleResultsFileUpload}
            maxCount={1}
          >
            <UploadOutlined className="upload-icon" />
            <p className="upload-text">
              Click or drag file to this area to upload
            </p>
            <p className="upload-hint">ZIP files only, up to 50MB</p>
          </Upload.Dragger>
        </div>

        <Form layout="vertical" className="upload-results-form">
          <Button
            type="primary"
            block
            size="large"
            onClick={handleResultsClick}
            className="upload-results-button"
          >
            View Results
          </Button>
        </Form>
      </div>
    </div>
  );
};

export default UploadResults;
