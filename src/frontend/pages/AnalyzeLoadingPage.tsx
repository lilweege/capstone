import { Button } from "@/components/ui/button";
import { Loader } from "lucide-react";
import { useNavigate } from "react-router-dom";

const AnalyzeLoadingPage = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-background">
      <div className="flex flex-col items-center space-y-6">
        <Loader className="animate-spin text-primary h-16 w-16" />
        <p className="text-muted-foreground text-center">
          Analyzing dataset. This might take a few hours. Results will be emailed to you.
        </p>
        <Button onClick={() => navigate("/")}>Analyze Another Dataset</Button>
      </div>
    </div>
  );
};

export default AnalyzeLoadingPage;