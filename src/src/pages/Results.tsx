import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Card } from "@/components/ui/card";
import { ChartContainer, ChartLegend, ChartTooltip } from "@/components/ui/chart";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip } from 'recharts';

// Interfaces for our data structures
interface SimilarityResult {
  file1: string;
  file2: string;
  similarityPercentage: number;
}

interface SimilarityStats {
  highestSimilarity: number;
  averageSimilarity: number;
  medianSimilarity: number;
  totalSubmissions: number;
}

const Results = () => {
  // Mock data for demonstration
  const mockResults: SimilarityResult[] = [
    { file1: "01022431.py", file2: "01141513.py", similarityPercentage: 100 },
    { file1: "02085216.py", file2: "02447653.py", similarityPercentage: 100 },
    { file1: "02951809.py", file2: "03234141.py", similarityPercentage: 95 },
    { file1: "04416985.py", file2: "08165126.py", similarityPercentage: 87 },
    { file1: "08316564.py", file2: "08909969.py", similarityPercentage: 75 },
  ].sort((a, b) => b.similarityPercentage - a.similarityPercentage);

  // Calculate statistics
  const stats: SimilarityStats = {
    highestSimilarity: Math.max(...mockResults.map(r => r.similarityPercentage)),
    averageSimilarity: Math.round(
      mockResults.reduce((acc, curr) => acc + curr.similarityPercentage, 0) / mockResults.length
    ),
    medianSimilarity: 79, // In real implementation, calculate this properly
    totalSubmissions: mockResults.length,
  };

  // Distribution data for the chart
  const distributionData = [
    { similarity: "0-10%", count: 0 },
    { similarity: "11-20%", count: 0 },
    { similarity: "21-30%", count: 1 },
    { similarity: "31-40%", count: 1 },
    { similarity: "41-50%", count: 2 },
    { similarity: "51-60%", count: 3 },
    { similarity: "61-70%", count: 4 },
    { similarity: "71-80%", count: 5 },
    { similarity: "81-90%", count: 8 },
    { similarity: "91-100%", count: 12 },
  ];

  return (
    <div className="min-h-screen bg-background p-8">
      <div className="container mx-auto">
        <div className="mb-8">
          <h1 className="text-3xl font-bold mb-2">Source Code Plagiarism Detection Report</h1>
          <p className="text-muted-foreground">Analysis results for submitted code files</p>
        </div>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <Card className="p-6">
            <h3 className="text-sm font-medium text-muted-foreground mb-2">Highest Similarity</h3>
            <p className="text-4xl font-bold text-primary">{stats.highestSimilarity}%</p>
          </Card>
          <Card className="p-6">
            <h3 className="text-sm font-medium text-muted-foreground mb-2">Average Similarity</h3>
            <p className="text-4xl font-bold">{stats.averageSimilarity}%</p>
            <p className="text-sm text-muted-foreground">Median: {stats.medianSimilarity}%</p>
          </Card>
          <Card className="p-6">
            <h3 className="text-sm font-medium text-muted-foreground mb-2">Total Submissions</h3>
            <p className="text-4xl font-bold">{stats.totalSubmissions}</p>
          </Card>
        </div>

        {/* Similarity Distribution Chart */}
        <Card className="p-6 mb-8">
          <h2 className="text-xl font-semibold mb-4">Similarity Distribution</h2>
          <div className="w-full aspect-[2/1] min-h-[400px]">
            <ChartContainer config={{}}>
              <BarChart
                data={distributionData}
                margin={{ top: 20, right: 30, left: 40, bottom: 60 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis
                  dataKey="similarity"
                  angle={-45}
                  textAnchor="end"
                  height={60}
                  interval={0}
                  tick={{ fontSize: 12 }}
                />
                <YAxis 
                  tick={{ fontSize: 12 }}
                />
                <Tooltip />
                <Bar 
                  dataKey="count" 
                  fill="#6366F1"
                  maxBarSize={50}
                />
              </BarChart>
            </ChartContainer>
          </div>
        </Card>

        {/* Submissions Table */}
        <Card className="mb-8">
          <div className="p-6">
            <h2 className="text-xl font-semibold mb-4">Similar Submissions</h2>
            <p className="text-sm text-muted-foreground mb-4">
              Highlights the most suspicious individual submissions, useful for exams
            </p>
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>File 1</TableHead>
                  <TableHead>File 2</TableHead>
                  <TableHead className="text-right">Similarity</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {mockResults.map((result, index) => (
                  <TableRow key={index}>
                    <TableCell className="font-medium">{result.file1}</TableCell>
                    <TableCell>{result.file2}</TableCell>
                    <TableCell className="text-right">
                      <span 
                        className={`inline-flex items-center justify-center px-2 py-1 rounded-full text-xs font-medium ${
                          result.similarityPercentage > 90 
                            ? 'bg-red-100 text-red-700' 
                            : result.similarityPercentage > 70 
                              ? 'bg-yellow-100 text-yellow-700' 
                              : 'bg-green-100 text-green-700'
                        }`}
                      >
                        {result.similarityPercentage}%
                      </span>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        </Card>
      </div>
    </div>
  );
};

export default Results;