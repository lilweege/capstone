import { api } from "./service/apiService";
import { useAuth0 } from "@auth0/auth0-react";

export const uploadFiles = async (files: FileList, analysisName: string) => {
  console.log("Uploading files...");
  const formData = new FormData();
  Array.from(files).forEach((file) => {
    formData.append("files", file);
  });

  formData.append("analysisName", analysisName);

  try {
    const response = await api.post("/upload", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
    return response.data;
  } catch (error) {
    console.error("Error uploading files:", error);
    return null;
  }
};
