from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import ChatMessage
from google import genai
from google.genai import types  # For GenerateContentConfig

# Create client with explicit API key
client = genai.Client(api_key=settings.GEMINI_API_KEY)

@csrf_exempt
def ai_chatbot(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '').strip()
        if not user_message:
            return JsonResponse({'reply': 'Please share your thoughts.'}, status=400)

        system_prompt = (
            "You are Sister Bot, a warm and empathetic AI supporter for HerRiseNow. "
            "You empower women and girls, focusing on gender equality, mentorship, counseling, "
            "and safety from violence. Respond with positivity, encouragement, and brevity. "
            "If danger is mentioned, urgently suggest the Red Emergency Button or helpline. "
            "Always end replies with a heart emoji 💜."
        )

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_message,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt
                )
            )
            ai_reply = response.text.strip()

            # Save to database
            session_id = request.session.session_key or 'anonymous'

            ChatMessage.objects.create(
                session_id=session_id,
                message=user_message,
                reply=ai_reply,
                user=request.user if request.user.is_authenticated else None
            )

            return JsonResponse({'reply': ai_reply})

        except Exception as e:
            print("Exact Gemini Error:", str(e))
            return JsonResponse({'reply': "Sister Bot is taking a quick break. Try our helpline meanwhile! 💜"}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)
# def ai_chatbot(request):
#     if request.method == 'POST':
#         user_message = request.POST.get('message', '').strip()
#         if not user_message:
#             return JsonResponse({'reply': 'Please share your thoughts.'}, status=400)

#         system_prompt = (
#             "You are Sister Bot, a warm and empathetic AI supporter for HerRiseNow. "
#             "You empower women and girls, focusing on gender equality, mentorship, counseling, "
#             "and safety from violence. Respond with positivity, encouragement, and brevity. "
#             "If danger is mentioned, urgently suggest the Red Emergency Button or helpline. "
#             "Always end replies with a heart emoji 💜."
#         )

#     try:
#     response = client.models.generate_content(
#         model="gemini-2.5-flash",  
#         contents=user_message,
#         config=types.GenerateContentConfig(
#             system_instruction=system_prompt
#         )
#     )
#     ai_reply = response.text.strip()

#     # ─── Add this right here ───
#     session_id = request.session.session_key or 'anonymous'

#     ChatMessage.objects.create(
#         session_id=session_id,
#         message=user_message,
#         reply=ai_reply,
#         user=request.user if request.user.is_authenticated else None
#     )
#     # ───────────────────────────

#     return JsonResponse({'reply': ai_reply})


#   except Exception as e:
#             print("Exact Gemini Error:", str(e))  # Check console for details
#             return JsonResponse({'reply': "Sister Bot is taking a quick break. Try our helpline meanwhile! 💜"}, status=500)

#     return JsonResponse({'error': 'Invalid request method.'}, status=405)
# # @csrf_exempt
# def ai_chatbot(request):
#     if request.method == 'POST':
#         user_message = request.POST.get('message', '').strip()
#         if not user_message:
#             return JsonResponse({'reply': 'Please share your thoughts.'}, status=400)

#         system_instruction = (
#             "You are Sister Bot, a warm and empathetic AI supporter for HerRiseNow. "
#             "You empower women and girls, focusing on gender equality, mentorship, counseling, "
#             "and safety from violence. Respond with positivity, encouragement, and brevity. "
#             "If danger is mentioned, urgently suggest the Red Emergency Button or helpline. "
#             "End replies with a heart emoji 💜."
#         )

#         try:
#             model = genai.GenerativeModel(
#                 model_name='gemini-2.5-flash',
#                 system_instruction=system_instruction
#             )

#             # ──────────────── ADD THE MEMORY CODE HERE ────────────────
#             if 'chat_history' not in request.session:
#                 request.session['chat_history'] = []

#             history = request.session['chat_history']
#             history.append({"role": "user", "parts": [user_message]})

#             chat = model.start_chat(history=history[-10:])  # Last 10 exchanges

#             response = chat.send_message(user_message)

#             ai_reply = response.text.strip()

#             history.append({"role": "model", "parts": [ai_reply]})
#             request.session['chat_history'] = history
#             # ──────────────────────────────────────────────────────────

#             return JsonResponse({'reply': ai_reply})

#         except Exception as e:
#             return JsonResponse({'reply': "Sister Bot is taking a quick break. Try our helpline! 💜"}, status=500)

#     return JsonResponse({'error': 'Invalid request method.'}, status=405)
# chatbot/views.py
