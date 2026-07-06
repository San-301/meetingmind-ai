from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

OUTPUT_FOLDER = "outputs"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def generate_pdf(results):

    pdf_path = os.path.join(OUTPUT_FOLDER, "Meeting_Report.pdf")

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("MeetingMind AI Report", styles["Title"]))

    # Summary
    story.append(Paragraph("Executive Summary", styles["Heading2"]))
    story.append(Paragraph(results["summary"], styles["BodyText"]))

    # Decisions
    story.append(Paragraph("Decisions", styles["Heading2"]))

    decisions = "<br/>".join(
        [f"• {d}" for d in results["decisions"]]
    )

    story.append(Paragraph(decisions, styles["BodyText"]))

    # Action Items
    story.append(Paragraph("Action Items", styles["Heading2"]))

    for item in results["action_items"]:

        text = (
            f"<b>Person:</b> {item['person']}<br/>"
            f"<b>Task:</b> {item['task']}<br/>"
            f"<b>Deadline:</b> {item['deadline']}<br/>"
            f"<b>Priority:</b> {item['priority']}<br/><br/>"
        )

        story.append(Paragraph(text, styles["BodyText"]))

    # Email
    story.append(Paragraph("Follow-up Email", styles["Heading2"]))
    story.append(Paragraph(results["email"], styles["BodyText"]))

    # Schedule
    story.append(Paragraph("Schedule", styles["Heading2"]))
    story.append(Paragraph(results["schedule"], styles["BodyText"]))

    doc.build(story)

    return pdf_path