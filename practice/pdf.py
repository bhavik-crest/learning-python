from fpdf import FPDF

class MuscleGainPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 12, 'Muscle Gain Guide (Workout + Nutrition)', ln=True, align='C')
        self.ln(8)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_text_color(0)
        self.cell(0, 10, title, ln=True)
        self.ln(4)

    def chapter_body(self, body, bold_terms=None):
        self.set_font('Arial', '', 12)
        self.set_text_color(50)

        if not bold_terms:
            self.multi_cell(0, 8, body)
            self.ln(6)
            return

        lines = body.split('\n')
        for line in lines:
            words = line.split(' ')
            for word in words:
                clean_word = word.strip(',.()')
                if clean_word in bold_terms:
                    self.set_font('Arial', 'B', 12)
                else:
                    self.set_font('Arial', '', 12)
                self.write(8, word + ' ')
            self.ln(10)
        self.ln(4)

    def meal_plan_table(self):
        col_widths = [40, 110, 30]
        start_x = self.get_x()
        start_y = self.get_y()
        row_height = 12  # Reduced row height for better fit
        font_size = 10  # Smaller font size for the table

        # Table header
        header = ['Meal', 'Food', 'Protein']
        self.set_font('Courier', 'B', font_size)

        # Header background color
        self.set_fill_color(200, 220, 255)
        self.rect(start_x, start_y, sum(col_widths), row_height, 'F')

        # Draw vertical lines for header
        x = start_x
        for w in col_widths:
            self.line(x, start_y, x, start_y + row_height)
            x += w
        self.line(start_x + sum(col_widths), start_y, start_x + sum(col_widths), start_y + row_height)

        # Draw horizontal lines top and bottom of header
        self.line(start_x, start_y, start_x + sum(col_widths), start_y)
        self.line(start_x, start_y + row_height, start_x + sum(col_widths), start_y + row_height)

        # Write header text centered vertically and horizontally
        self.set_xy(start_x, start_y + 4)
        for i, col in enumerate(header):
            self.cell(col_widths[i], 6, col, border=0, align='C')

        # Move cursor to first row start
        y = start_y + row_height

        # Table rows data
        rows = [
            ['Breakfast', '1 cup oats + 2 tbsp peanut butter + 200ml milk + chia seeds', '~20g'],
            ['Mid-morning', 'Whey protein shake (1 scoop)', '~25g'],
            ['Lunch', '1 cup cooked dal + 100g paneer + 1 multigrain roti', '~30g'],
            ['Snack', 'Handful almonds (15g), 1 fruit', '~7g'],
            ['Evening', 'Sprouted moong salad with tofu or boiled chickpeas', '~15g'],
            ['Dinner', '1 cup rajma/chole + brown rice + curd', '~25g'],
        ]

        self.set_font('Courier', '', font_size)

        for row in rows:
            x = start_x

            # Draw horizontal line top of the row
            self.line(start_x, y, start_x + sum(col_widths), y)

            # Draw vertical lines for the row
            for w in col_widths:
                self.line(x, y, x, y + row_height)
                x += w
            self.line(start_x + sum(col_widths), y, start_x + sum(col_widths), y + row_height)

            # Write Meal column with padding (left 4, top 4)
            self.set_xy(start_x + 4, y + 4)
            self.cell(col_widths[0] - 8, 6, row[0], border=0)

            # Food column with wrapped text
            self.set_xy(start_x + col_widths[0] + 4, y + 4)
            start_multi_y = self.get_y()
            self.multi_cell(col_widths[1] - 8, 6, row[1], border=0)
            end_multi_y = self.get_y()
            multi_cell_height = end_multi_y - start_multi_y

            # Protein column vertically centered based on multi_cell height
            protein_y = y + (multi_cell_height / 2) - 3
            self.set_xy(start_x + col_widths[0] + col_widths[1] + 4, protein_y)
            self.cell(col_widths[2] - 8, 6, row[2], border=0)

            # Move y to next row position (max of row_height or wrapped cell height)
            y += max(multi_cell_height, row_height)

        # Draw bottom line of last row
        self.line(start_x, y, start_x + sum(col_widths), y)

        # Add space after table
        self.set_y(y + 10)


pdf = MuscleGainPDF()
pdf.add_page()

# Protein Needs Section
pdf.chapter_title("How Much Protein You Need")
pdf.chapter_body(
    "To gain muscle fast, especially when you start training again, you should aim for:\n\n"
    "2.0 - 2.2 grams of protein per kg of body weight.\n\n"
    "So for 60 kg:\n"
    "Minimum target: 60 x 2.0 = 120g/day\n"
    "Maximum effective target: 60 x 2.2 = 132g/day\n\n"
    "Recommended for you: approximately 125g protein per day.\n\n"
    "You can split this across 4 to 6 meals/snacks: about 20-30g protein per meal.",
    bold_terms=["2.0", "2.2", "60", "Minimum", "Maximum", "Recommended", "125g", "4", "6", "20-30g"]
)

# Meal Plan Table
pdf.chapter_title("Meal Plan")
pdf.meal_plan_table()

# Protein Supplement Tips Section
pdf.chapter_title("Protein Supplement Tips")
pdf.chapter_body(
    "If you are okay with dairy:\n"
    "- Use whey protein (concentrate or isolate) post-workout or with breakfast/snack.\n"
    "- Brand examples (India): Optimum Nutrition (ON), Myprotein, MuscleBlaze, etc.\n\n"
    "If you want to avoid all animal products:\n"
    "- Use plant-based protein (pea, soy, rice blend).",
    bold_terms=["whey protein", "plant-based protein"]
)

# Muscle Gain Strategy Section
pdf.chapter_title("Muscle Gain Strategy")
pdf.chapter_body(
    "Since you are not training currently, here is what you should do:\n\n"
    "- Restart strength training 3 to 4 times per week.\n"
    "- Focus on compound bodyweight exercises (push-ups, squats, pull-ups) if no gym.\n"
    "- Or return to gym gradually.\n"
    "- Progressive overload: increase reps, weights, or sets weekly.\n"
    "- Maintain a high-protein diet as above.\n"
    "- Get 8 or more hours of sleep daily.",
    bold_terms=["strength training", "compound bodyweight exercises", "Progressive overload", "high-protein diet", "8 or more hours"]
)

# Workout Routine Section
pdf.chapter_title("Bodyweight Workout Plan (No Equipment)")
pdf.chapter_body(
    "Push-Ups (Chest, Shoulders, Triceps, Core):\n"
    "- 3 sets x 8-12 reps, rest 60-90 seconds.\n"
    "- Progression: Knee -> Incline -> Standard -> Diamond -> Decline -> One-Arm.\n\n"
    "Squats (Legs, Glutes, Core):\n"
    "- 3 to 4 sets x 15-20 reps, rest 60 seconds.\n"
    "- Progression: Bodyweight -> Goblet -> Bulgarian Split -> Pistol Squat.\n\n"
    "Pull-Ups (Back, Biceps, Shoulders):\n"
    "- 3 sets x 4-8 reps, rest 90 seconds.\n"
    "- Use band-assisted or negatives if needed.",
    bold_terms=["Push-Ups", "Squats", "Pull-Ups", "sets", "reps", "rest", "Progression"]
)

# Weekly Training Schedule Section
pdf.chapter_title("Weekly Training Schedule")
pdf.chapter_body(
    "Monday: Push-Ups + Squats\n"
    "Tuesday: Pull-Ups + Core\n"
    "Wednesday: Rest or Walking\n"
    "Thursday: Push-Ups + Squats (increase reps)\n"
    "Friday: Pull-Ups + Core\n"
    "Saturday: Full-body (All 3 exercises)\n"
    "Sunday: Rest or Yoga/Stretching",
    bold_terms=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
)

pdf.output("Muscle_Gain_Workout_and_Nutrition_Guide.pdf")