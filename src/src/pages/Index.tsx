import Navbar from "@/components/Navbar";
import Features from "@/components/Features";
import { Button } from "@/components/ui/button";
import { ArrowRight } from "lucide-react";

const Index = () => {
  return (
    <div className="min-h-screen">
      <Navbar />
      
      {/* Hero Section */}
      <section className="pt-24 pb-20 bg-gradient-to-b from-white to-gray-50">
        <div className="container mx-auto px-4">
          <div className="max-w-3xl mx-auto text-center">
            <h1 className="text-5xl font-bold mb-8 bg-clip-text text-transparent bg-gradient-to-r from-primary to-blue-600">
              Verify Academic and Contest Submissions
            </h1>
            <p className="text-xl text-gray-600 mb-10">
              Empower educators and contest administrators with advanced AI-powered plagiarism detection. Ensure the integrity of student work and competition submissions.
            </p>
            <div className="flex gap-4 justify-center">
              <Button size="lg" className="bg-primary hover:bg-primary/90">
                Get Started
                <ArrowRight className="ml-2 h-5 w-5" />
              </Button>
              <Button size="lg" variant="outline">
                Learn More
              </Button>
            </div>
          </div>
        </div>
      </section>

      <Features />

      {/* How It Works Section */}
      <section className="py-20">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl font-bold text-center mb-12">
            How It Works
          </h2>
          <div className="max-w-3xl mx-auto">
            <div className="space-y-8">
              {[
                { step: "1", text: "Upload student or contestant submissions" },
                { step: "2", text: "Our AI analyzes content against extensive databases" },
                { step: "3", text: "Review detailed originality reports" },
              ].map((item) => (
                <div key={item.step} className="flex items-center gap-4">
                  <div className="h-10 w-10 rounded-full bg-primary text-white flex items-center justify-center font-bold">
                    {item.step}
                  </div>
                  <p className="text-lg">{item.text}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-50 py-12">
        <div className="container mx-auto px-4">
          <div className="text-center text-gray-600">
            <p>© 2024 SyntaxSentinals. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Index;