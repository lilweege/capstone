import { Button } from "@/components/ui/button";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="fixed w-full bg-white/80 backdrop-blur-md z-50 border-b">
      <div className="container mx-auto px-4 py-3 flex justify-between items-center">
        <Link to="/" className="text-2xl font-bold text-primary">
          SyntaxSentinals
        </Link>
        <div className="flex gap-4 items-center">
          <Button className="bg-primary hover:bg-primary/90" asChild>
            <Link to="/login">Log In</Link>
          </Button>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;