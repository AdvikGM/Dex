# 🧠 FEATURE 1: NATURAL LANGUAGE INTERCEPTOR WITH LONG-TERM MEMORY CONTEXT
        else:
            try:
                prompt_config = {
                    "system_instruction": (
                        f"You are Dex, an energetic personal assistant bot engineered by 12-year-old developer Advik. "
                        f"Keep responses concise, fun, and conversational. Use emojis frequently. If the user asks about "
                        f"adding tasks or math, remind them they can use structural prefixes like 'Add [task]' or 'calc [math]'!\n\n"
                        f"⚡ CRITICAL SYSTEM INSTRUCTION:\n"
                        f"Below is the recent logged conversation history retrieved from your SQLite database. "
                        f"Use this data context to remember facts the user shared with you in past messages:\n"
                        f"=== DATABASE MEMORY MATRIX ===\n{history_context}\n============================="
                    )
                }
                
                # 🎯 Pointed to the correct stable SDK model name to fix the 404 error
                response = self.ai_client.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=clean_input,
                    config=prompt_config
                )
                return response.text
                
            except Exception as e:
                print(f"⚠️ Neural Network Connection Glitch: {e}")
                return "I lost sync with my central AI grid matrix, but my local routing framework is up! Try typing 'Help'."
