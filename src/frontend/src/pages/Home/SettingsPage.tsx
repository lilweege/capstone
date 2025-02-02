import React, { useState, useEffect } from "react";
import { InputNumber, Button, Form, Typography, Row, Col } from "antd";
import "./SettingsPage.css";

const { Title, Paragraph } = Typography;

const SettingsPage: React.FC = () => {
  const [threshold, setThreshold] = useState<number | null>(null);

  useEffect(() => {
    // Load the threshold value from local storage when the component mounts
    const savedThreshold = localStorage.getItem("plagiarismThreshold");
    if (savedThreshold) {
      setThreshold(Number(savedThreshold));
    }
  }, []);

  const handleSave = () => {
    if (threshold !== null) {
      localStorage.setItem("plagiarismThreshold", threshold.toString());
      alert("Settings saved successfully!");
    }
  };

  return (
    <div className="settings-container">
      <Row justify="center" align="middle" className="settings-row">
        <Col xs={24} sm={20} md={16} lg={12} xl={10} className="settings-card">
          <div className="mb-8">
            <Title level={2}>Settings</Title>
            <Paragraph>Configure your plagiarism detection preferences</Paragraph>
          </div>

          <Form layout="vertical">
            <Form.Item label="Plagiarism Threshold (%)" required>
              <InputNumber
                min={0}
                max={100}
                value={threshold}
                onChange={(value) => setThreshold(value)}
                style={{ width: "100%" }}
              />
            </Form.Item>

            <Button type="primary" block size="large" onClick={handleSave}>
              Save Settings
            </Button>
          </Form>
        </Col>
      </Row>
    </div>
  );
};

export default SettingsPage;