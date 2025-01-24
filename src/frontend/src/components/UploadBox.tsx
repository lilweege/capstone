import { Input, message, List, Button } from 'antd';
import { InboxOutlined, CloseOutlined } from '@ant-design/icons';
import React, { useState, useEffect } from 'react';

const UploadBox = ({ onFileListChange }) => {
  const [fileList, setFileList] = useState([]);

  useEffect(() => {
    const handleWindowDrop = (e) => {
      e.preventDefault();
      const files = Array.from(e.dataTransfer.files);
      handleFiles(files);
    };

    const handleWindowDragOver = (e) => {
      e.preventDefault();
    };

    window.addEventListener('drop', handleWindowDrop);
    window.addEventListener('dragover', handleWindowDragOver);

    return () => {
      window.removeEventListener('drop', handleWindowDrop);
      window.removeEventListener('dragover', handleWindowDragOver);
    };
  }, []);

  const handleFiles = (files) => {
    setFileList((prevFileList) => {
      const newFileList = [...prevFileList, ...files];
      if (onFileListChange) {
        onFileListChange(newFileList);
      }
      return newFileList;
    });

    message.success(`${files.length} file(s) uploaded successfully.`);
  };

  const handleFileChange = (e) => {
    const files = Array.from(e.target.files);
    handleFiles(files);
  };

  const handleRemoveFile = (fileToRemove) => {
    setFileList((prevFileList) => {
      const newFileList = prevFileList.filter(file => file !== fileToRemove);
      if (onFileListChange) {
        onFileListChange(newFileList);
      }
      return newFileList;
    });
  };

  return (
    <div style={{ padding: '20px', border: '1px dashed #d9d9d9', borderRadius: '4px', textAlign: 'center' }}>
      <InboxOutlined style={{ fontSize: '32px', color: '#1890ff' }} />
      <p>Click or drag file to this area to upload</p>
      <p>Support for multiple file uploads. Only accept .zip or .py files.</p>
      <Input
        type="file"
        accept=".zip,.py"
        onChange={handleFileChange}
        multiple
        style={{ display: 'none' }}
        id="file-upload"
      />
      <label htmlFor="file-upload" style={{ cursor: 'pointer', color: '#1890ff' }}>
        Browse Files
      </label>
      <List
        style={{ marginTop: '20px', maxHeight: '200px', overflowY: 'auto' }}
        bordered
        dataSource={fileList}
        renderItem={item => (
          <List.Item
            actions={[
              <Button
                type="text"
                icon={<CloseOutlined />}
                onClick={() => handleRemoveFile(item)}
              />
            ]}
          >
            {item.name}
          </List.Item>
        )}
      />
    </div>
  );
};

export default UploadBox;