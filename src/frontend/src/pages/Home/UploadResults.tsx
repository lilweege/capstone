import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Button, Upload, Typography, Form } from "antd";
import { UploadOutlined } from "@ant-design/icons";
import "./UploadResults.css"; // Custom CSS for styling
import UploadBox from "@/components/UploadBox";

const { Title, Paragraph } = Typography;

const UploadResults: React.FC = () => {
  const navigate = useNavigate();
  const [resultsFile, setResultsFile] = useState<File | null>(null);

  const handleResultsFileUpload = (file) => {
    setResultsFile(file);
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

        <UploadBox onFileListChange={handleResultsFileUpload} mode="results" />

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
