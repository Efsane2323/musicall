from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafΔ±ndan dΓΌzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://images.app.goo.gl/MTLXTSDCA4MLHScP7",
                caption=(f"""β π¬πΎπππΊπ»πΊ {message.from_user.mention} \n\nβ π‘πΎπ {bot} !\n\nβ π²πΎπππ π²πππ»πΎπππΎππ½πΎ mΓΌzik π’πΊππΊπ»πππΎπ π‘ππππ . . ! \n\nβ π‘πΊπ πΈπΎππππππ, π²πΎπ πΈπππΎπππ πΈπΎπππππ ππΎπππ π πππππΊππ π¦πππ»πΊ π€πππΎπππ . . !"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π π‘πΎππ π¦πππ»πΊ π€πππΎ π", url=f"http://t.me/hababam_sinifibot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π πͺππππππΊπ" , callback_data= "herkes"
                    ),
                    InlineKeyboardButton(
                        "πΉπ· π²πΊπππ", url="https://t.me/hababammsinifi"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["djej", f"djej@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text("β π­ππ :\n\n π‘ππππ π ππππΏ π’πΊπππππΊππ ππΌππ π²π π΄πΌ ππΎπππππΎ ππππππΊπΌπ π΅πΊππ½ππ :\n\n> π¬πΎππΊπππΊππ π²ππππΎ ,\n> π‘πΊπππΊπππ π£πΊππΎπ π€πππΎ ,\n> π²πΎπππ π²πππ»πΎπ πΈπππΎπππΎ ,", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "π π³ππ πͺππππππΊπ", callback_data="cbbilgi")
                 ],[
                     InlineKeyboardButton(
                         "π―οΈ π ππΊ π¬πΎππ ", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "π© πππ‘π’π©", url="https://t.me/hababammsinifi")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text("β π­ππ :\n\n π‘ππππ π ππππΏ π’πΊπππππΊππ ππΌππ π²π π΄πΌ ππΎπππππΎ ππππππΊπΌπ π΅πΊππ½ππ :\n\n> π¬πΎππΊπππΊππ π²ππππΎ ,\n> π‘πΊπππΊπππ π£πΊππΎπ π€πππΎ ,\n> π²πΎπππ π²πππ»πΎπ πΈπππΎπππΎ ,", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "π π³ππ πͺππππππΊπ", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "π―οΈ π ππΊ π¬πΎππ", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "π© πππ‘π’π©", url="https://t.me/hababammsinifi")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>\nΒ» /vbul => α΄ Ιͺα΄α΄α΄ ΙͺΙ΄α΄ΙͺΚ . \nΒ» /bul => α΄α΄α΄’Ιͺα΄ ΙͺΙ΄α΄ΙͺΚ . \nΒ» /oynat => α΄α΄α΄’Ιͺα΄ α΄ΚΙ΄α΄α΄ . \nΒ» /durdur => α΄α΄α΄’ΙͺΙ’Ιͺ α΄α΄Κα΄α΄Κ . \nΒ» /devam => α΄α΄α΄’ΙͺΙ’Ιͺ sα΄Κα΄α΄Κ . \nΒ» /atla =>  α΄α΄α΄’ΙͺΙ’Ιͺ α΄α΄Κα΄ . \nΒ» /son => α΄α΄α΄’ΙͺΙ’Ιͺ sα΄Ι΄Κα΄Ι΄α΄ΙͺΚ . \nΒ» /katil => α΄sΙͺsα΄α΄Ι΄Ιͺ Ι’Κα΄Κα΄ α΄α΄α΄ α΄α΄ α΄α΄α΄Κ . \nΒ» /reload => α΄α΄α΄ΙͺΙ΄ ΚΙͺsα΄α΄sΙͺΙ΄Ιͺ Ι’α΄Ι΄α΄α΄ΚΚα΄Κ .</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "πΉπ· π πππππΊπ", url="hababammusicAsistann")
                 ],
                 [
                     InlineKeyboardButton(
                         "β¬οΈ π¦πΎππ β¬οΈ", callback_data="cbstart")
                 ] 
             ]
         )
         )

@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!\nBu botun adminler iΓ§in komut menΓΌsΓΌ π€©\n\n βΆοΈ /devam - ΕarkΔ± Γ§almaya devam et\n βΈοΈ /durdur - Γ§alan parΓ§ayΔ± duraklatmak iΓ§in\n π /atla- SΔ±raya alΔ±nmΔ±Ε mΓΌzik parΓ§asΔ±nΔ± atlatΔ±r.\n βΉ /son - mΓΌzik Γ§almayΔ± durdurma\n πΌ /ver botun sadece yΓΆnetici iΓ§in kullanΔ±labilir olan komutlarΔ±nΔ± kullanabilmesi iΓ§in kullanΔ±cΔ±ya yetki ver\n π½ /al botun yΓΆnetici komutlarΔ±nΔ± kullanabilen kullanΔ±cΔ±nΔ±n yetkisini al\n\n βͺ /asistan - MΓΌzik asistanΔ± grubunuza katΔ±lΔ±r.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "β GeliΕtirici", url="https://t.me/hababammsinifi")
                 ],
                 [
                     InlineKeyboardButton(
                         "β¬οΈ Geri β¬οΈ", callback_data="herkes")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""β π¬πΎπππΊπ»πΊ {query.from_user.mention} \n\nβ π‘πΎπ {bot} !\n\nβ π²πΎπππ π²πππ»πΎπππΎππ½πΎ mΓΌzik π’πΊππΊπ»πππΎπ π‘ππππ . . ! \n\nβ π‘πΊπ πΈπΎππππππ, π²πΎπ πΈπππΎπππ πΈπΎπππππ ππΎπππ π πππππΊππ π¦πππ»πΊ π€πππΎπππ . . !""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π π‘πΎππ π¦πππ»πΊ π€πππΎ π", url=f"http://t.me/hababam_sinifibot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π πͺππππππΊπ" , callback_data= "herkes"
                    ),
                    InlineKeyboardButton(
                        "πΉπ· π²πΊπππ", url=f"https://t.me/hababammsinifi"
                    )
                ]
                
           ]
        ),
    )
