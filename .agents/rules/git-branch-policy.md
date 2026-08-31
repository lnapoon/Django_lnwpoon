# Git Branching Policy & Rules

## ⚠️ CRITICAL RULE: ห้ามแก้ไขโค้ดหรือทำงานบน branch `main` โดยเด็ดขาด

1. **ห้ามทำงานบน branch `main`**:
   - ห้ามแก้ไขไฟล์, เพิ่มโค้ด, หรือ commit โดยตรงบน branch `main`
2. **ทำงานผ่าน branch `dev` หรือ feature branch เสมอ**:
   - การแก้ไขโค้ด, พัฒนาฟีเจอร์ใหม่, หรือแก้ไข bug ให้ทำบน branch `dev` หรือแตก branch ใหม่เท่านั้น (เช่น `feature/...`, `fix/...`)
3. **ตรวจสอบ branch ก่อนเริ่มงาน**:
   - ก่อนจะเริ่มแก้ไขหรือสร้างไฟล์ใหม่ ให้ตรวจสอบ branch ปัจจุบันเสมอ (`git branch --show-current`) หากพบว่าอยู่ที่ `main` ให้ checkout ไปยัง `dev` หรือสร้าง branch ใหม่ก่อนเสมอ
