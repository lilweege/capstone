import { Button } from "@/components/common/button";
import { Input } from "@/components/common/input";
import { Label } from "@/components/common/label";
import { Upload } from "lucide-react";
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth0 } from "@auth0/auth0-react";
import Navbar from "@/components/Navbar/Navbar";

const Home = () => {
  const navigate = useNavigate();
  const [resultsFile, setResultsFile] = useState<File | null>(null);
  const { isAuthenticated } = useAuth0();

  if (!isAuthenticated) {
    navigate("/");
  }

  const handleFileUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      // Handle file upload logic here
      console.log("Analysis dataset uploaded:", file);
    }
  };

  const handleAnalyzeClick = () => {
    // Navigate to the Loading Page
    console.log("Analyzing dataset...");
    navigate("/loading");
  };

  const handleResultsFileUpload = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    const file = event.target.files?.[0];
    if (file) {
      setResultsFile(file);
      console.log("Results file uploaded:", file);
    }
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
    <div className="bg-background min-h-screen">
      <Navbar />

      <div className="pt-16 container mx-auto px-4 py-6">
        <div className="flex flex-col md:flex-row gap-8">
          <div className="flex-1 space-y-6">
            <div className="bg-card rounded-lg p-6 shadow-sm">
              <h2 className="text-2xl font-semibold mb-4">Analyze a dataset</h2>
              <p className="text-muted-foreground mb-6">
                Upload a dataset to analyze for potential code plagiarism.
              </p>

              <div className="space-y-4">
                <div className="border-2 border-dashed border-input rounded-lg p-6 text-center">
                  <Upload className="mx-auto h-12 w-12 text-muted-foreground mb-4" />
                  <Label htmlFor="analysis-upload" className="cursor-pointer">
                    <span className="text-muted-foreground">
                      Upload a file or drag and drop
                    </span>
                  </Label>
                  <Input
                    id="analysis-upload"
                    type="file"
                    accept=".zip"
                    className="hidden"
                    onChange={handleFileUpload}
                  />
                  <p className="text-sm text-muted-foreground mt-2">
                    ZIP files only, up to 50MB
                  </p>
                </div>

                <div className="space-y-4">
                  <div>
                    <Label htmlFor="analysis-name">Analysis name</Label>
                    <Input
                      id="analysis-name"
                      placeholder="Enter a name for this analysis"
                      className="mt-1"
                    />
                  </div>

                  <Button className="w-full" onClick={handleAnalyzeClick}>
                    Analyze Dataset
                  </Button>
                </div>
              </div>
            </div>
          </div>

          <div className="flex-1 space-y-6">
            <div className="bg-card rounded-lg p-6 shadow-sm">
              <h2 className="text-2xl font-semibold mb-4">View Results</h2>
              <p className="text-muted-foreground mb-6">
                Check the analysis results of your previous submissions by
                uploading the results ZIP file emailed to you.
              </p>

              <div className="space-y-4">
                <div className="border-2 border-dashed border-input rounded-lg p-6 text-center">
                  <Upload className="mx-auto h-12 w-12 text-muted-foreground mb-4" />
                  <Label htmlFor="results-upload" className="cursor-pointer">
                    <span className="text-muted-foreground">
                      Upload a file or drag and drop
                    </span>
                  </Label>
                  <Input
                    id="results-upload"
                    type="file"
                    accept=".zip"
                    className="hidden"
                    onChange={handleResultsFileUpload}
                  />
                  <p className="text-sm text-muted-foreground mt-2">
                    ZIP files only, up to 50MB
                  </p>
                </div>

                <div className="space-y-4">
                  <Button className="w-full" onClick={handleResultsClick}>
                    View Results
                  </Button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
