import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Clock, Search, User, Calendar } from "lucide-react";
import { Link } from "react-router-dom";

interface BlogPost {
  id: number;
  title: string;
  excerpt: string;
  author: {
    name: string;
    avatar?: string;
  };
  category: string;
  readTime: number;
  publishedAt: string;
  coverImage?: string;
}

const blogPosts: BlogPost[] = [
  {
    id: 1,
    title: "Understanding Your Dominant Cognitive Function",
    excerpt: "Explore how your dominant function shapes your personality and decision-making process in daily life.",
    author: { name: "Dr. Sarah Chen" },
    category: "Cognitive Functions",
    readTime: 8,
    publishedAt: "2024-01-15",
  },
  {
    id: 2,
    title: "MBTI and Career Success: Finding Your Path",
    excerpt: "Discover how understanding your MBTI type can guide you toward a fulfilling career that matches your natural strengths.",
    author: { name: "Michael Rodriguez" },
    category: "Career Development",
    readTime: 12,
    publishedAt: "2024-01-10",
  },
  {
    id: 3,
    title: "The Shadow Functions: Your Hidden Potential",
    excerpt: "Jung's concept of shadow functions and how developing them can lead to personal growth and better relationships.",
    author: { name: "Dr. Emily Watson" },
    category: "Jungian Psychology",
    readTime: 15,
    publishedAt: "2024-01-08",
  },
  {
    id: 4,
    title: "Introverted vs Extraverted Thinking",
    excerpt: "A deep dive into the differences between Ti and Te, and how these functions manifest in different personality types.",
    author: { name: "James Thompson" },
    category: "Cognitive Functions",
    readTime: 10,
    publishedAt: "2024-01-05",
  },
  {
    id: 5,
    title: "Building Better Relationships Through Type Compatibility",
    excerpt: "Learn how understanding cognitive functions can improve your relationships and communication with others.",
    author: { name: "Dr. Lisa Park" },
    category: "Relationships",
    readTime: 7,
    publishedAt: "2024-01-03",
  },
  {
    id: 6,
    title: "The Evolution of Personality Theory",
    excerpt: "From Jung to Myers-Briggs to modern cognitive function theory - a historical perspective on personality psychology.",
    author: { name: "Prof. David Miller" },
    category: "Psychology History",
    readTime: 20,
    publishedAt: "2024-01-01",
  }
];

export default function Blogs() {
  const [searchTerm, setSearchTerm] = useState("");
  const [selectedCategory, setSelectedCategory] = useState("All");

  const categories = ["All", "Cognitive Functions", "Career Development", "Jungian Psychology", "Relationships", "Psychology History"];

  const filteredPosts = blogPosts.filter(post => {
    const matchesSearch = post.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         post.excerpt.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         post.author.name.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesCategory = selectedCategory === "All" || post.category === selectedCategory;
    return matchesSearch && matchesCategory;
  });

  return (
    <div className="container mx-auto px-4 py-8">
      {/* Header */}
      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold mb-4">Psychology Insights</h1>
        <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
          Expert articles on cognitive functions, MBTI, Jungian psychology, and personal development
        </p>
      </div>

      {/* Search and Filter */}
      <div className="mb-8 space-y-4">
        <div className="relative max-w-md mx-auto">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-muted-foreground h-4 w-4" />
          <Input
            placeholder="Search articles..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="pl-10"
          />
        </div>

        <div className="flex flex-wrap justify-center gap-2">
          {categories.map((category) => (
            <Button
              key={category}
              variant={selectedCategory === category ? "psychology" : "outline"}
              size="sm"
              onClick={() => setSelectedCategory(category)}
            >
              {category}
            </Button>
          ))}
        </div>
      </div>

      {/* Blog Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {filteredPosts.map((post) => (
          <Card key={post.id} className="group hover:shadow-card transition-all duration-300 hover:-translate-y-1 overflow-hidden">
            {/* Cover Image Placeholder */}
            <div className="h-48 bg-hero-gradient flex items-center justify-center">
              <div className="text-white text-6xl font-bold opacity-20">
                {post.category.charAt(0)}
              </div>
            </div>

            <CardContent className="p-6 space-y-4">
              {/* Category Badge */}
              <Badge variant="secondary" className="text-xs">
                {post.category}
              </Badge>

              {/* Title and Excerpt */}
              <div className="space-y-2">
                <h3 className="text-xl font-semibold group-hover:text-psychology-blue transition-colors line-clamp-2">
                  {post.title}
                </h3>
                <p className="text-muted-foreground text-sm line-clamp-3">
                  {post.excerpt}
                </p>
              </div>

              {/* Author and Meta */}
              <div className="flex items-center justify-between pt-4 border-t">
                <div className="flex items-center space-x-3">
                  <Avatar className="h-8 w-8">
                    <AvatarImage src={post.author.avatar} />
                    <AvatarFallback className="text-xs bg-psychology-blue text-white">
                      {post.author.name.split(' ').map(n => n[0]).join('')}
                    </AvatarFallback>
                  </Avatar>
                  <div>
                    <p className="text-sm font-medium">{post.author.name}</p>
                    <div className="flex items-center space-x-2 text-xs text-muted-foreground">
                      <Calendar className="h-3 w-3" />
                      <span>{new Date(post.publishedAt).toLocaleDateString()}</span>
                      <Clock className="h-3 w-3" />
                      <span>{post.readTime} min read</span>
                    </div>
                  </div>
                </div>
              </div>

              {/* Read More Button */}
              <Button variant="outline" size="sm" className="w-full mt-4" asChild>
                <Link to={`/blog/${post.id}`}>
                  Read Article
                </Link>
              </Button>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Empty State */}
      {filteredPosts.length === 0 && (
        <div className="text-center py-12">
          <Search className="h-12 w-12 mx-auto text-muted-foreground mb-4" />
          <h3 className="text-xl font-semibold mb-2">No articles found</h3>
          <p className="text-muted-foreground">
            Try adjusting your search terms or category filter
          </p>
        </div>
      )}
    </div>
  );
}