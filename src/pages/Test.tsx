import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { Label } from "@/components/ui/label";
import { Checkbox } from "@/components/ui/checkbox";
import { Progress } from "@/components/ui/progress";
import { Brain, CheckCircle, Clock } from "lucide-react";
import { Link } from "react-router-dom";

interface Question {
  id: number;
  text: string;
  options: string[];
  multipleChoice?: boolean;
}

const sampleQuestions: Question[] = [
  {
    id: 1,
    text: "When making decisions, you primarily rely on:",
    options: [
      "Logical analysis and objective facts",
      "Personal values and how it affects others",
      "Past experiences and proven methods",
      "Future possibilities and innovative approaches"
    ]
  },
  {
    id: 2,
    text: "In social situations, you tend to:",
    options: [
      "Seek out new people and conversations",
      "Prefer intimate conversations with close friends",
      "Observe first before participating",
      "Take charge and organize activities"
    ]
  },
  {
    id: 3,
    text: "Which activities energize you most? (You can choose multiple answers)",
    options: [
      "Brainstorming creative solutions",
      "Helping others solve problems",
      "Working alone on detailed tasks",
      "Leading team projects"
    ],
    multipleChoice: true
  }
];

export default function Test() {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState<Record<number, string | string[]>>({});
  const [isComplete, setIsComplete] = useState(false);
  const [testStarted, setTestStarted] = useState(false);

  const progress = ((currentQuestion + 1) / sampleQuestions.length) * 100;

  const handleAnswer = (questionId: number, answer: string | string[]) => {
    setAnswers(prev => ({ ...prev, [questionId]: answer }));
  };

  const nextQuestion = () => {
    if (currentQuestion < sampleQuestions.length - 1) {
      setCurrentQuestion(prev => prev + 1);
    } else {
      setIsComplete(true);
    }
  };

  const startTest = () => {
    setTestStarted(true);
  };

  if (!testStarted) {
    return (
      <div className="container mx-auto px-4 py-16 text-center">
        <div className="max-w-2xl mx-auto space-y-8">
          <div className="space-y-4">
            <Brain className="h-20 w-20 mx-auto text-psychology-blue" />
            <h1 className="text-4xl font-bold">Cognitive Function Assessment</h1>
            <p className="text-xl text-muted-foreground">
              Discover your unique cognitive function stack through our advanced ML-powered assessment.
            </p>
          </div>

          <Card className="shadow-card">
            <CardContent className="p-8 space-y-6">
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6 text-center">
                <div className="space-y-2">
                  <Clock className="h-8 w-8 mx-auto text-psychology-purple" />
                  <h3 className="font-semibold">15-20 Minutes</h3>
                  <p className="text-sm text-muted-foreground">Average completion time</p>
                </div>
                <div className="space-y-2">
                  <CheckCircle className="h-8 w-8 mx-auto text-psychology-purple" />
                  <h3 className="font-semibold">60+ Questions</h3>
                  <p className="text-sm text-muted-foreground">Comprehensive analysis</p>
                </div>
                <div className="space-y-2">
                  <Brain className="h-8 w-8 mx-auto text-psychology-purple" />
                  <h3 className="font-semibold">AI Powered</h3>
                  <p className="text-sm text-muted-foreground">Machine learning analysis</p>
                </div>
              </div>

              <div className="space-y-3 text-left">
                <h3 className="font-semibold">What to expect:</h3>
                <ul className="space-y-2 text-sm text-muted-foreground">
                  <li>• Objective and subjective questions about your preferences</li>
                  <li>• Scenario-based questions to assess cognitive patterns</li>
                  <li>• Some questions allow multiple answers</li>
                  <li>• Instant results with detailed cognitive function breakdown</li>
                </ul>
              </div>

              <Button variant="psychology" size="xl" onClick={startTest} className="w-full">
                Begin Assessment
              </Button>
            </CardContent>
          </Card>
        </div>
      </div>
    );
  }

  if (isComplete) {
    return (
      <div className="container mx-auto px-4 py-16">
        <div className="max-w-4xl mx-auto text-center space-y-8">
          <div className="space-y-4">
            <CheckCircle className="h-20 w-20 mx-auto text-psychology-purple" />
            <h1 className="text-4xl font-bold">You are an ENFP!</h1>
            <p className="text-xl text-muted-foreground">
              The Campaigner - Enthusiastic, creative, and sociable free spirits
            </p>
          </div>

          <Card className="shadow-card">
            <CardHeader>
              <CardTitle>Your Cognitive Function Stack</CardTitle>
            </CardHeader>
            <CardContent className="space-y-6">
              {[
                { function: "Ne", name: "Extraverted Intuition", strength: 95, color: "bg-psychology-blue" },
                { function: "Fi", name: "Introverted Feeling", strength: 88, color: "bg-psychology-purple" },
                { function: "Te", name: "Extraverted Thinking", strength: 45, color: "bg-psychology-mint" },
                { function: "Si", name: "Introverted Sensing", strength: 25, color: "bg-muted" }
              ].map((func, index) => (
                <div key={func.function} className="space-y-2">
                  <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-3">
                      <Badge className="font-mono">{func.function}</Badge>
                      <span className="font-medium">{func.name}</span>
                      {index === 0 && <Badge variant="secondary">Dominant</Badge>}
                      {index === 1 && <Badge variant="outline">Auxiliary</Badge>}
                    </div>
                    <span className="text-sm font-medium">{func.strength}%</span>
                  </div>
                  <div className="w-full bg-secondary rounded-full h-4">
                    <div 
                      className={`${func.color} h-4 rounded-full transition-all duration-1000`}
                      style={{ width: `${func.strength}%` }}
                    />
                  </div>
                </div>
              ))}
            </CardContent>
          </Card>

          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button variant="psychology" size="lg" asChild>
              <Link to="/profile">View Full Profile</Link>
            </Button>
            <Button variant="outline" size="lg">
              Download Results
            </Button>
          </div>
        </div>
      </div>
    );
  }

  const question = sampleQuestions[currentQuestion];

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="max-w-2xl mx-auto">
        {/* Progress */}
        <div className="mb-8">
          <div className="flex justify-between text-sm text-muted-foreground mb-2">
            <span>Question {currentQuestion + 1} of {sampleQuestions.length}</span>
            <span>{Math.round(progress)}% Complete</span>
          </div>
          <Progress value={progress} className="h-2" />
        </div>

        {/* Question */}
        <Card className="shadow-card">
          <CardHeader>
            <CardTitle className="text-xl">{question.text}</CardTitle>
            {question.multipleChoice && (
              <Badge variant="secondary" className="w-fit">
                Multiple answers allowed
              </Badge>
            )}
          </CardHeader>
          <CardContent className="space-y-4">
            {question.multipleChoice ? (
              <div className="space-y-3">
                {question.options.map((option, index) => (
                  <div key={index} className="flex items-center space-x-2">
                    <Checkbox 
                      id={`option-${index}`}
                      onCheckedChange={(checked) => {
                        const currentAnswers = (answers[question.id] as string[]) || [];
                        if (checked) {
                          handleAnswer(question.id, [...currentAnswers, option]);
                        } else {
                          handleAnswer(question.id, currentAnswers.filter(a => a !== option));
                        }
                      }}
                    />
                    <Label htmlFor={`option-${index}`} className="flex-1 cursor-pointer p-3 border rounded-lg hover:bg-accent">
                      {option}
                    </Label>
                  </div>
                ))}
              </div>
            ) : (
              <RadioGroup 
                value={answers[question.id] as string || ""}
                onValueChange={(value) => handleAnswer(question.id, value)}
              >
                {question.options.map((option, index) => (
                  <div key={index} className="flex items-center space-x-2">
                    <RadioGroupItem value={option} id={`option-${index}`} />
                    <Label htmlFor={`option-${index}`} className="flex-1 cursor-pointer p-3 border rounded-lg hover:bg-accent">
                      {option}
                    </Label>
                  </div>
                ))}
              </RadioGroup>
            )}

            <Button 
              onClick={nextQuestion}
              disabled={!answers[question.id]}
              className="w-full"
              variant="psychology"
            >
              {currentQuestion === sampleQuestions.length - 1 ? "Complete Assessment" : "Next Question"}
            </Button>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}