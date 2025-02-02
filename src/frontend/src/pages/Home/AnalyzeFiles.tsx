import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Button, Input, Typography, Form, Row, Col } from "antd";
import "./AnalyzeFiles.css";
import UploadBox from "@/components/UploadBox";
import { uploadFiles } from "@/services/ssApi";

const { Title, Paragraph } = Typography;

const AnalyzeFiles: React.FC = () => {
  const navigate = useNavigate();
  const [analysisFile, setAnalysisFile] = useState(null);

  const handleFileUpload = (file) => {
    setAnalysisFile(file);
  };

  const handleAnalyzeClick = async () => {
    if (!analysisFile) {
      window.alert("Please upload a dataset file first.");
      return;
    }

    try {
      const response = await uploadFiles(analysisFile, "analyze");
      navigate("/home");
    } catch (error) {
      console.error("Error uploading files:", error);
    }
  };

  return (
    <div className="analyze-container">
      <Row justify="center" align="middle" className="analyze-row">
        <Col xs={24} sm={20} md={16} lg={12} xl={10} className="analyze-card">
          <Title level={2} className="analyze-title">
            Analyze a Dataset
          </Title>
          <Paragraph className="analyze-description">
            Upload a dataset to analyze for potential code plagiarism. Use a ZIP
            file containing your project files.
          </Paragraph>

          <UploadBox onFileListChange={handleFileUpload} mode="analyze" />

          <Form layout="vertical" className="analyze-form">
            <Form.Item label="Analysis Name" name="analysisName">
              <Input
                placeholder="Enter a name for this analysis"
                size="large"
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
  );
};

export default AnalyzeFiles;
