import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Button, Input, Upload, Typography, Form, Row, Col } from "antd";
import { UploadOutlined } from "@ant-design/icons";
import "./AnalyzeFiles.css";

const { Title, Paragraph } = Typography;

const AnalyzeFiles: React.FC = () => {
  const navigate = useNavigate();
  const [analysisFile, setAnalysisFile] = useState<File | null>(null);

  const handleFileUpload = (file: File) => {
    setAnalysisFile(file);
    console.log("Analysis dataset uploaded:", file);
    return false; // Prevents automatic upload
  };

  const handleAnalyzeClick = () => {
    if (!analysisFile) {
      window.alert("Please upload a dataset file first.");
      return;
    }
    console.log("Analyzing dataset...");
    navigate("/loading");
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

          <div className="analyze-upload">
            <Upload.Dragger
              name="file"
              accept=".zip"
              beforeUpload={handleFileUpload}
              maxCount={1}
            >
              <UploadOutlined className="upload-icon" />
              <p className="upload-text">
                Click or drag file to this area to upload
              </p>
              <p className="upload-hint">Only ZIP files, up to 50MB</p>
            </Upload.Dragger>
          </div>

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
