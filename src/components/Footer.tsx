import { Brain, Github, Twitter, Instagram, LinkedinIcon } from "lucide-react";
import { Link } from "react-router-dom";

export const Footer = () => {
  return (
    <footer className="bg-secondary/20 border-t mt-auto">
      <div className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          {/* Brand */}
          <div className="space-y-3">
            <div className="flex items-center space-x-3">
              <div className="w-8 h-8 bg-hero-gradient rounded-lg flex items-center justify-center">
                <Brain className="h-5 w-5 text-white" />
              </div>
              <span className="text-xl font-bold bg-hero-gradient bg-clip-text text-transparent">
                CogniStack
              </span>
            </div>
            <p className="text-sm text-muted-foreground">
              Discover your cognitive potential through Jungian psychology and MBTI assessment.
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h3 className="font-semibold mb-3">Quick Links</h3>
            <div className="space-y-2">
              <Link to="/" className="block text-sm text-muted-foreground hover:text-foreground">
                Home
              </Link>
              <Link to="/test" className="block text-sm text-muted-foreground hover:text-foreground">
                Take Test
              </Link>
              <Link to="/blogs" className="block text-sm text-muted-foreground hover:text-foreground">
                Blogs
              </Link>
              <Link to="/about" className="block text-sm text-muted-foreground hover:text-foreground">
                About
              </Link>
            </div>
          </div>

          {/* Resources */}
          <div>
            <h3 className="font-semibold mb-3">Resources</h3>
            <div className="space-y-2">
              <Link to="/about#faq" className="block text-sm text-muted-foreground hover:text-foreground">
                FAQ
              </Link>
              <Link to="/profile" className="block text-sm text-muted-foreground hover:text-foreground">
                Profile
              </Link>
              <Link to="/about#contact" className="block text-sm text-muted-foreground hover:text-foreground">
                Contact
              </Link>
            </div>
          </div>

          {/* Social Links */}
          <div>
            <h3 className="font-semibold mb-3">Connect</h3>
            <div className="flex space-x-4">
              <a href="#" className="text-muted-foreground hover:text-psychology-blue transition-colors">
                <Github className="h-5 w-5" />
              </a>
              <a href="#" className="text-muted-foreground hover:text-psychology-blue transition-colors">
                <Twitter className="h-5 w-5" />
              </a>
              <a href="#" className="text-muted-foreground hover:text-psychology-blue transition-colors">
                <Instagram className="h-5 w-5" />
              </a>
              <a href="#" className="text-muted-foreground hover:text-psychology-blue transition-colors">
                <LinkedinIcon className="h-5 w-5" />
              </a>
            </div>
          </div>
        </div>

        <div className="border-t mt-8 pt-8 text-center">
          <p className="text-sm text-muted-foreground">
            © 2024 CogniStack. Built with psychology and technology.
          </p>
        </div>
      </div>
    </footer>
  );
};