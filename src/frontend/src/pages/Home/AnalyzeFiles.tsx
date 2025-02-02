import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Button, Input, Typography, Form, Row, Col, Spin, message } from "antd";
import "./AnalyzeFiles.css";
import UploadBox from "@/components/UploadBox";
import { uploadFiles } from "@/services/ssApi";

const { Title, Paragraph } = Typography;

const AnalyzeFiles: React.FC = () => {
  const navigate = useNavigate();
  const [analysisFile, setAnalysisFile] = useState(null);
  const [isDragging, setIsDragging] = useState(false);
  const [analysisName, setAnalysisName] = useState("");
  const [formKey, setFormKey] = useState(0); // Add a key to force re-render
  const [clearFiles, setClearFiles] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [loadingMessage, setLoadingMessage] = useState(
    "Preparing your results..."
  );

  // Drag Event Handlers
  useEffect(() => {
    const handleDragEnter = () => setIsDragging(true);
    const handleDragOver = (event: DragEvent) => {
      event.preventDefault(); // Allow drop
    };
    const handleDragLeave = (event: DragEvent) => {
      if (event.relatedTarget === null) setIsDragging(false);
    };
    const handleDrop = (event: DragEvent) => {
      event.preventDefault();
      setIsDragging(false);

      if (event.dataTransfer?.files.length) {
        const file = event.dataTransfer.files[0];
        handleFileUpload(file);
      }
    };

    document.addEventListener("dragenter", handleDragEnter);
    document.addEventListener("dragover", handleDragOver);
    document.addEventListener("dragleave", handleDragLeave);
    document.addEventListener("drop", handleDrop);

    return () => {
      document.removeEventListener("dragenter", handleDragEnter);
      document.removeEventListener("dragover", handleDragOver);
      document.removeEventListener("dragleave", handleDragLeave);
      document.removeEventListener("drop", handleDrop);
    };
  }, []);

  const handleFileUpload = (file) => {
    setAnalysisFile(file);
  };

  const handleAnalyzeClick = async () => {
    if (!analysisFile || analysisFile.length === 0) {
      window.alert("Please upload a dataset file first.");
      return;
    }

    if (!analysisName) {
      window.alert("Please enter a name for this analysis.");
      return;
    }

    try {
      // set loading state
      message.success(
        "Analysis started successfully. You'll receive an email with the results once it's done!"
      );
      setIsLoading(true);
      setLoadingMessage("Preparing your results...");

      // Cycle through messages
      setTimeout(() => {
        setLoadingMessage("You can close the window and wait for the email!");
      }, 3000); // Change message after 3 seconds

      setAnalysisFile(null);
      setAnalysisName("");
      setFormKey((prevKey) => prevKey + 1);
      setClearFiles(true);
      const response = await uploadFiles(analysisFile, analysisName);
      if (!response) {
        setIsLoading(false);
        message.error(
          "Analysis failed to start. Please try again or contact support."
        );
        return;
      }
      if (response.data) {
        const results = response.data;
        localStorage.setItem("resultsData", JSON.stringify(results));
        navigate("/results");
      }
    } catch (error) {
      console.error("Error uploading files:", error);
    }
  };

  return (
    <>
      {isDragging && (
        <div className="drop-overlay">
          <p className="drop-message">Drop your files here</p>
        </div>
      )}
      {isLoading ? (
        <div className="loading-container">
          <Spin size="large" />
          <p className="loading-message fade">{loadingMessage}</p>
        </div>
      ) : (
        <div className="analyze-container">
          <Row justify="center" align="middle" className="analyze-row">
            <Col
              xs={24}
              sm={20}
              md={16}
              lg={12}
              xl={10}
              className="analyze-card"
            >
              <Title level={2} className="analyze-title">
                Analyze a Dataset
              </Title>
              <Paragraph className="analyze-description">
                Upload a dataset to analyze for potential code plagiarism. Use a
                ZIP file containing your project files.
              </Paragraph>

              <UploadBox
                onFileListChange={handleFileUpload}
                mode="analyze"
                clearFiles={clearFiles}
                setClearFiles={setClearFiles}
              />

              <Form key={formKey} layout="vertical" className="analyze-form">
                <Form.Item label="Analysis Name" name="analysisName" required>
                  <Input
                    placeholder="Enter a name for this analysis"
                    size="large"
                    value={analysisName}
                    onChange={(e) => setAnalysisName(e.target.value)}
                  />
                </Form.Item>

                <Button
                  type="primary"
                  block
                  size="large"
                  onClick={handleAnalyzeClick}
                  className="analyze-button"
                >
                  Analyze Dataset
                </Button>
              </Form>
            </Col>
          </Row>
        </div>
      )}
    </>
  );
};

export default AnalyzeFiles;
