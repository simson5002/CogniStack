import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Badge } from "@/components/ui/badge";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Edit3, Brain, Heart, Star, Users } from "lucide-react";

export default function Profile() {
  const [user] = useState({
    name: "Alex Thompson",
    username: "@alexthompson",
    email: "alex@example.com",
    mbtiType: "ENFP",
    avatar: "",
    cognitiveStack: [
      { function: "Ne", name: "Extraverted Intuition", strength: 95, dominant: true },
      { function: "Fi", name: "Introverted Feeling", strength: 88, auxiliary: true },
      { function: "Te", name: "Extraverted Thinking", strength: 45, tertiary: true },
      { function: "Si", name: "Introverted Sensing", strength: 25, inferior: true }
    ]
  });

  const famousPersonalities = [
    { name: "Robin Williams", image: "", profession: "Actor/Comedian" },
    { name: "Walt Disney", image: "", profession: "Entrepreneur" },
    { name: "Mark Twain", image: "", profession: "Writer" },
    { name: "Ellen DeGeneres", image: "", profession: "TV Host" }
  ];

  const compatibilityData = [
    { type: "INFJ", compatibility: 95, relationship: "Ideal Match" },
    { type: "INTJ", compatibility: 88, relationship: "Great Friend" },
    { type: "ENFJ", compatibility: 82, relationship: "Good Partner" },
    { type: "ENTP", compatibility: 75, relationship: "Fun Companion" }
  ];

  return (
    <div className="container mx-auto px-4 py-8 space-y-8">
      {/* Profile Header */}
      <Card className="shadow-card">
        <CardContent className="p-6">
          <div className="flex flex-col md:flex-row items-start md:items-center space-y-4 md:space-y-0 md:space-x-6">
            <div className="relative">
              <Avatar className="h-24 w-24">
                <AvatarImage src={user.avatar} />
                <AvatarFallback className="text-2xl bg-hero-gradient text-white">
                  {user.name.split(' ').map(n => n[0]).join('')}
                </AvatarFallback>
              </Avatar>
              <Button size="icon" className="absolute -bottom-2 -right-2 h-8 w-8 rounded-full">
                <Edit3 className="h-4 w-4" />
              </Button>
            </div>
            
            <div className="flex-1">
              <div className="flex items-center space-x-3 mb-2">
                <h1 className="text-3xl font-bold">{user.name}</h1>
                <Badge variant="secondary" className="text-lg px-3 py-1">
                  {user.mbtiType}
                </Badge>
              </div>
              <p className="text-muted-foreground mb-1">{user.username}</p>
              <p className="text-sm text-muted-foreground">{user.email}</p>
              
              <Button variant="outline" className="mt-4">
                <Edit3 className="h-4 w-4 mr-2" />
                Edit Profile
              </Button>
            </div>
          </div>
        </CardContent>
      </Card>

      <Tabs defaultValue="cognitive" className="space-y-6">
        <TabsList className="grid w-full grid-cols-3">
          <TabsTrigger value="cognitive">Cognitive Stack</TabsTrigger>
          <TabsTrigger value="famous">Famous Types</TabsTrigger>
          <TabsTrigger value="compatibility">Compatibility</TabsTrigger>
        </TabsList>

        {/* Cognitive Functions */}
        <TabsContent value="cognitive">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center">
                <Brain className="h-5 w-5 mr-2" />
                Your Cognitive Function Stack
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              {user.cognitiveStack.map((func, index) => (
                <div key={func.function} className="space-y-2">
                  <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-3">
                      <Badge 
                        variant={func.dominant ? "default" : func.auxiliary ? "secondary" : "outline"}
                        className="font-mono"
                      >
                        {func.function}
                      </Badge>
                      <span className="font-medium">{func.name}</span>
                      {func.dominant && <Star className="h-4 w-4 text-psychology-purple" />}
                    </div>
                    <span className="text-sm font-medium">{func.strength}%</span>
                  </div>
                  <div className="w-full bg-secondary rounded-full h-3">
                    <div 
                      className="bg-hero-gradient h-3 rounded-full transition-all duration-500"
                      style={{ width: `${func.strength}%` }}
                    />
                  </div>
                </div>
              ))}
            </CardContent>
          </Card>
        </TabsContent>

        {/* Famous Personalities */}
        <TabsContent value="famous">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center">
                <Star className="h-5 w-5 mr-2" />
                Famous {user.mbtiType} Personalities
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                {famousPersonalities.map((person, index) => (
                  <Card key={index} className="text-center p-4 hover:shadow-card transition-shadow">
                    <Avatar className="h-20 w-20 mx-auto mb-3">
                      <AvatarFallback className="bg-psychology-blue text-white text-lg">
                        {person.name.split(' ').map(n => n[0]).join('')}
                      </AvatarFallback>
                    </Avatar>
                    <h3 className="font-semibold">{person.name}</h3>
                    <p className="text-sm text-muted-foreground">{person.profession}</p>
                  </Card>
                ))}
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Compatibility */}
        <TabsContent value="compatibility">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center">
                <Heart className="h-5 w-5 mr-2" />
                Relationship Compatibility
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {compatibilityData.map((compat, index) => (
                  <div key={compat.type} className="flex items-center justify-between p-4 border rounded-lg">
                    <div className="flex items-center space-x-4">
                      <Badge variant="outline" className="font-mono">
                        {compat.type}
                      </Badge>
                      <div>
                        <p className="font-medium">{compat.relationship}</p>
                        <p className="text-sm text-muted-foreground">
                          {compat.compatibility}% compatibility
                        </p>
                      </div>
                    </div>
                    <div className="w-24 bg-secondary rounded-full h-2">
                      <div 
                        className="bg-psychology-purple h-2 rounded-full"
                        style={{ width: `${compat.compatibility}%` }}
                      />
                    </div>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  );
}