import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Brain, Users, BookOpen, Target } from "lucide-react";
import { Link } from "react-router-dom";
import heroImage from "@/assets/hero-psychology.jpg";

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen">
      {/* Hero Section */}
      <section className="relative h-screen flex items-center justify-center overflow-hidden">
        <div 
          className="absolute inset-0 bg-cover bg-center"
          style={{ backgroundImage: `url(${heroImage})` }}
        />
        <div className="absolute inset-0 bg-black/40" />
        
        <div className="relative z-10 text-center space-y-6 px-4 max-w-4xl mx-auto">
          <h1 className="text-5xl md:text-7xl font-bold text-white animate-fade-up">
            Discover Your
            <span className="block bg-gradient-to-r from-psychology-mint to-white bg-clip-text text-transparent">
              Cognitive Stack
            </span>
          </h1>
          
          <p className="text-xl md:text-2xl text-white/90 max-w-2xl mx-auto animate-fade-up">
            Unlock the power of your mind through Jungian Cognitive Functions and 
            advanced MBTI assessment powered by machine learning.
          </p>
          
          <div className="flex flex-col sm:flex-row gap-4 justify-center animate-fade-up">
            <Button variant="hero" size="xl" asChild>
              <Link to="/auth">Start Your Journey</Link>
            </Button>
            <Button variant="glass" size="xl" asChild>
              <Link to="/about">Learn More</Link>
            </Button>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 px-4">
        <div className="container mx-auto max-w-6xl">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold mb-4">Why Choose CogniStack?</h2>
            <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
              Advanced psychology meets cutting-edge technology for the most accurate 
              personality assessment available.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {[
              {
                icon: Brain,
                title: "AI-Powered Analysis",
                description: "Machine learning algorithms analyze your cognitive patterns with unprecedented accuracy."
              },
              {
                icon: Target,
                title: "Jungian Framework",
                description: "Based on Carl Jung's cognitive function theory and modern MBTI research."
              },
              {
                icon: Users,
                title: "Personality Matching",
                description: "Discover your compatibility with others and famous personalities."
              },
              {
                icon: BookOpen,
                title: "Expert Insights",
                description: "Access articles and blogs from psychology professionals and researchers."
              }
            ].map((feature, index) => (
              <Card key={index} className="group hover:shadow-card transition-all duration-300 hover:-translate-y-2">
                <CardContent className="p-6 text-center">
                  <div className="w-16 h-16 bg-hero-gradient rounded-full flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform">
                    <feature.icon className="h-8 w-8 text-white" />
                  </div>
                  <h3 className="text-xl font-semibold mb-3">{feature.title}</h3>
                  <p className="text-muted-foreground">{feature.description}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-subtle-gradient">
        <div className="container mx-auto max-w-4xl text-center px-4">
          <h2 className="text-4xl font-bold mb-6">Ready to Understand Yourself?</h2>
          <p className="text-xl text-muted-foreground mb-8">
            Join thousands of users who have discovered their true cognitive potential.
          </p>
          <Button variant="psychology" size="xl" asChild>
            <Link to="/auth">Take the Assessment</Link>
          </Button>
        </div>
      </section>
    </div>
  );
}