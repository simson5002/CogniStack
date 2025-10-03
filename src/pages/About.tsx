import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
import { Badge } from "@/components/ui/badge";
import { Brain, Target, Users, Lightbulb, Github, Twitter, Instagram, LinkedinIcon } from "lucide-react";

export default function About() {
  const faqData = [
    {
      question: "What is CogniStack?",
      answer: "CogniStack is an advanced self-development platform that uses machine learning to assess your Jungian Cognitive Functions and provide insights into your MBTI personality type. We combine scientific psychology with modern technology to give you the most accurate personality assessment available."
    },
    {
      question: "How accurate is the assessment?",
      answer: "Our ML-powered assessment achieves over 90% accuracy by analyzing both subjective preferences and objective behavioral patterns. The system uses advanced algorithms trained on thousands of verified personality profiles to provide precise cognitive function analysis."
    },
    {
      question: "What are Cognitive Functions?",
      answer: "Cognitive Functions are mental processes identified by Carl Jung that describe how we perceive and process information. There are 8 functions: Ne, Ni, Se, Si (perceiving) and Te, Ti, Fe, Fi (judging). Each person has a unique 'stack' of 4 functions that determine their personality type."
    },
    {
      question: "How is this different from other MBTI tests?",
      answer: "Unlike simple questionnaires, CogniStack uses machine learning to analyze cognitive patterns, provides detailed function strength analysis, and offers personalized insights including compatibility matching and career guidance based on your unique cognitive profile."
    },
    {
      question: "Is my data secure?",
      answer: "Yes, we take privacy seriously. All assessment data is encrypted and stored securely. We never share individual results with third parties, and you have full control over your profile visibility and data."
    }
  ];

  return (
    <div className="container mx-auto px-4 py-8 space-y-16">
      {/* Hero Section */}
      <section className="text-center space-y-6">
        <h1 className="text-4xl md:text-6xl font-bold bg-hero-gradient bg-clip-text text-transparent">
          About CogniStack
        </h1>
        <p className="text-xl text-muted-foreground max-w-3xl mx-auto">
          Bridging the gap between ancient psychological wisdom and modern technology 
          to unlock human potential through deep self-understanding.
        </p>
      </section>

      {/* Mission & Vision */}
      <section className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <Card className="shadow-card">
          <CardHeader>
            <CardTitle className="flex items-center">
              <Target className="h-6 w-6 mr-3 text-psychology-blue" />
              Our Mission
            </CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-muted-foreground leading-relaxed">
              To democratize access to deep psychological insights by combining Carl Jung's 
              groundbreaking work on cognitive functions with cutting-edge machine learning. 
              We believe everyone deserves to understand their unique mental architecture and 
              use that knowledge to build a more fulfilling life.
            </p>
          </CardContent>
        </Card>

        <Card className="shadow-card">
          <CardHeader>
            <CardTitle className="flex items-center">
              <Lightbulb className="h-6 w-6 mr-3 text-psychology-purple" />
              Our Vision
            </CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-muted-foreground leading-relaxed">
              A world where individuals understand their cognitive strengths and growth areas, 
              leading to better relationships, career satisfaction, and personal development. 
              We envision psychology-informed decision making becoming as common as 
              using data in business.
            </p>
          </CardContent>
        </Card>
      </section>

      {/* What We Do */}
      <section>
        <h2 className="text-3xl font-bold text-center mb-12">What Makes Us Different</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {[
            {
              icon: Brain,
              title: "ML-Powered Analysis",
              description: "Our algorithms don't just categorize - they measure the strength of each cognitive function with scientific precision.",
              badge: "AI Technology"
            },
            {
              icon: Users,
              title: "Comprehensive Compatibility",
              description: "Discover not just your type, but how you interact with all 16 types in relationships, work, and friendships.",
              badge: "Relationship Science"
            },
            {
              icon: Target,
              title: "Actionable Insights",
              description: "Move beyond labels to practical guidance for career choices, personal growth, and communication strategies.",
              badge: "Practical Application"
            }
          ].map((feature, index) => (
            <Card key={index} className="text-center shadow-card hover:shadow-elegant transition-shadow">
              <CardContent className="p-6 space-y-4">
                <div className="w-16 h-16 bg-hero-gradient rounded-full flex items-center justify-center mx-auto">
                  <feature.icon className="h-8 w-8 text-white" />
                </div>
                <Badge variant="secondary">{feature.badge}</Badge>
                <h3 className="text-xl font-semibold">{feature.title}</h3>
                <p className="text-muted-foreground">{feature.description}</p>
              </CardContent>
            </Card>
          ))}
        </div>
      </section>

      {/* The Science Behind It */}
      <section className="bg-subtle-gradient p-8 rounded-2xl">
        <h2 className="text-3xl font-bold text-center mb-8">The Science Behind CogniStack</h2>
        <div className="max-w-4xl mx-auto space-y-6">
          <p className="text-lg leading-relaxed">
            Our platform is built on over 100 years of psychological research, starting with Carl Jung's 
            revolutionary work on psychological types in 1921. We've enhanced this foundation with:
          </p>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-8">
            <div className="space-y-3">
              <h3 className="text-xl font-semibold">Jungian Foundation</h3>
              <ul className="space-y-2 text-muted-foreground">
                <li>• 8 cognitive functions theory</li>
                <li>• Psychological type dynamics</li>
                <li>• Shadow function development</li>
                <li>• Individuation process insights</li>
              </ul>
            </div>
            <div className="space-y-3">
              <h3 className="text-xl font-semibold">Modern Enhancements</h3>
              <ul className="space-y-2 text-muted-foreground">
                <li>• Machine learning pattern recognition</li>
                <li>• Behavioral data analysis</li>
                <li>• Statistical validation methods</li>
                <li>• Continuous algorithm improvement</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* FAQ Section */}
      <section>
        <h2 className="text-3xl font-bold text-center mb-12">Frequently Asked Questions</h2>
        <div className="max-w-3xl mx-auto">
          <Accordion type="single" collapsible className="space-y-4">
            {faqData.map((faq, index) => (
              <AccordionItem key={index} value={`item-${index}`} className="border rounded-lg px-4">
                <AccordionTrigger className="text-left font-semibold">
                  {faq.question}
                </AccordionTrigger>
                <AccordionContent className="text-muted-foreground leading-relaxed">
                  {faq.answer}
                </AccordionContent>
              </AccordionItem>
            ))}
          </Accordion>
        </div>
      </section>

      {/* Connect Section */}
      <section className="text-center space-y-6">
        <h2 className="text-3xl font-bold">Connect With Us</h2>
        <p className="text-muted-foreground max-w-2xl mx-auto">
          Join our community of psychology enthusiasts, researchers, and individuals 
          committed to personal growth and understanding.
        </p>
        
        <div className="flex justify-center space-x-6">
          <a 
            href="#" 
            className="w-12 h-12 bg-psychology-blue rounded-full flex items-center justify-center text-white hover:bg-psychology-purple transition-colors"
          >
            <Github className="h-6 w-6" />
          </a>
          <a 
            href="#" 
            className="w-12 h-12 bg-psychology-blue rounded-full flex items-center justify-center text-white hover:bg-psychology-purple transition-colors"
          >
            <Twitter className="h-6 w-6" />
          </a>
          <a 
            href="#" 
            className="w-12 h-12 bg-psychology-blue rounded-full flex items-center justify-center text-white hover:bg-psychology-purple transition-colors"
          >
            <Instagram className="h-6 w-6" />
          </a>
          <a 
            href="#" 
            className="w-12 h-12 bg-psychology-blue rounded-full flex items-center justify-center text-white hover:bg-psychology-purple transition-colors"
          >
            <LinkedinIcon className="h-6 w-6" />
          </a>
        </div>
      </section>
    </div>
  );
}