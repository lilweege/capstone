import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { Button } from "@/components/ui/button";
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { Slider } from "@/components/ui/slider";
import { Switch } from "@/components/ui/switch";
import { useToast } from "@/components/ui/use-toast";

const formSchema = z.object({
  similarityThreshold: z.number().min(0).max(100),
  minLineCount: z.number().min(1),
  enableAutoDetection: z.boolean(),
});

type SettingsFormValues = z.infer<typeof formSchema>;

const defaultValues: SettingsFormValues = {
  similarityThreshold: 70,
  minLineCount: 10,
  enableAutoDetection: true,
};

const Settings = () => {
  const { toast } = useToast();
  const form = useForm<SettingsFormValues>({
    resolver: zodResolver(formSchema),
    defaultValues,
  });

  function onSubmit(data: SettingsFormValues) {
    // In a real app, this would persist to backend/localStorage
    console.log("Settings saved:", data);
    toast({
      title: "Settings updated",
      description: "Your preferences have been saved successfully.",
    });
  }

  return (
    <div className="min-h-screen bg-background p-8">
      <div className="container max-w-2xl mx-auto">
        <div className="mb-8">
          <h1 className="text-3xl font-bold mb-2">Settings</h1>
          <p className="text-muted-foreground">
            Configure your plagiarism detection preferences
          </p>
        </div>

        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
            <FormField
              control={form.control}
              name="similarityThreshold"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Similarity Threshold (%)</FormLabel>
                  <FormControl>
                    <div className="space-y-4">
                      <Slider
                        min={0}
                        max={100}
                        step={1}
                        value={[field.value]}
                        onValueChange={(vals) => field.onChange(vals[0])}
                      />
                      <div className="text-sm text-muted-foreground">
                        Current value: {field.value}%
                      </div>
                    </div>
                  </FormControl>
                  <FormDescription>
                    Submissions with similarity above this threshold will be flagged
                    as potential plagiarism
                  </FormDescription>
                </FormItem>
              )}
            />

            <FormField
              control={form.control}
              name="minLineCount"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Minimum Line Count</FormLabel>
                  <FormControl>
                    <Input
                      type="number"
                      {...field}
                      onChange={(e) => field.onChange(Number(e.target.value))}
                    />
                  </FormControl>
                  <FormDescription>
                    Minimum number of lines required for comparison
                  </FormDescription>
                </FormItem>
              )}
            />

            <FormField
              control={form.control}
              name="enableAutoDetection"
              render={({ field }) => (
                <FormItem className="flex flex-row items-center justify-between rounded-lg border p-4">
                  <div className="space-y-0.5">
                    <FormLabel className="text-base">
                      Automatic Detection
                    </FormLabel>
                    <FormDescription>
                      Automatically scan new submissions for potential plagiarism
                    </FormDescription>
                  </div>
                  <FormControl>
                    <Switch
                      checked={field.value}
                      onCheckedChange={field.onChange}
                    />
                  </FormControl>
                </FormItem>
              )}
            />

            <Button type="submit">Save Settings</Button>
          </form>
        </Form>
      </div>
    </div>
  );
};

export default Settings;